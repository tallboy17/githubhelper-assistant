import faiss
import numpy as np
import google.generativeai as genai
#from google import genai
import os
import json
import logging
import uuid
from datetime import datetime, timezone

from flask import Flask, request, jsonify
from flask_cors import CORS # For handling Cross-Origin Resource Sharing

# --- Flask App Initialization ---
app = Flask(__name__)
CORS(app) # Enable CORS for all routes (adjust as needed for specific origins)

# --- Configure Logging ---
# Logging will be configured after config is loaded
logger = logging.getLogger(__name__)

# Global variables to store the loaded config, FAISS index, ID mapping, prompt template, and LLM model
app_config = None
faiss_index = None
faiss_id_to_doc_id_map = []
prompt_template = None
llm_model = None

# --- 0. Load Configuration ---
def load_config(config_path="config.json"):
    """Loads configuration from a JSON file."""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        logger.info(f"Configuration loaded from {config_path}")
        return config
    except FileNotFoundError:
        logger.error(f"Error: Config file not found at {config_path}. Please create it.")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON config file: {e}")
        raise

# --- 0.1. Configure the Gemini API ---
def configure_gemini(api_key_env_var, embedding_model, llm_model_name):
    """Configures the Gemini API and initializes the LLM model."""
    global llm_model
    gemini_api_key = os.getenv(api_key_env_var)

    if not gemini_api_key:
        logger.error(f"ERROR: Gemini API key not found. Please set the '{api_key_env_var}' environment variable.")
        raise ValueError(f"Gemini API key not found in environment variable: {api_key_env_var}")

    genai.configure(api_key=gemini_api_key)
    logger.info("Gemini API configured.")

    try:
        llm_model = genai.GenerativeModel(llm_model_name)
        logger.info(f"Gemini Generative Model '{llm_model_name}' initialized.")
    except Exception as e:
        logger.error(f"Failed to initialize Gemini Generative Model '{llm_model_name}': {e}")
        raise

# --- Function to Load Prompt Template ---
def load_prompt_template(filepath):
    """Loads the prompt template string from a specified file."""
    if not os.path.exists(filepath):
        logger.error(f"Prompt template file '{filepath}' not found.")
        raise FileNotFoundError(f"Prompt template file '{filepath}' not found.")
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            template = f.read()
        logger.info(f"Prompt template loaded from {filepath}")
        return template
    except Exception as e:
        logger.error(f"Error reading prompt template file {filepath}: {e}")
        raise

# --- 1. Load FAISS Index and Mapping ---
def load_faiss_artifacts(index_file, map_file):
    """Loads the FAISS index and the FAISS ID to Document ID mapping."""
    global faiss_index, faiss_id_to_doc_id_map

    if not os.path.exists(index_file):
        logger.error(f"FAISS index file '{index_file}' not found. Please run index_creator.py first.")
        raise FileNotFoundError(f"FAISS index file '{index_file}' not found.")
    if not os.path.exists(map_file):
        logger.error(f"Mapping file '{map_file}' not found. Please run index_creator.py first.")
        raise FileNotFoundError(f"Mapping file '{map_file}' not found.")

    try:
        faiss_index = faiss.read_index(index_file)
        logger.info(f"FAISS index loaded from {index_file} with {faiss_index.ntotal} vectors.")

        with open(map_file, 'r', encoding='utf-8') as f:
            faiss_id_to_doc_id_map = json.load(f)
        logger.info(f"FAISS ID to Document ID mapping loaded from {map_file} (Total entries: {len(faiss_id_to_doc_id_map)}).")
        
        if faiss_index.ntotal != len(faiss_id_to_doc_id_map):
            logger.warning("Mismatch: FAISS index vector count does not match mapping entry count. Index might be stale.")
            # Depending on strictness, this could be an error or just a warning.
            # For an API, you might want to raise an error to prevent inconsistent behavior.
            # For now, it's a warning.
            pass

        return True
    except Exception as e:
        logger.error(f"Error loading FAISS artifacts: {e}")
        raise

# --- 2. Retrieve Document Content by ID ---
def get_document_content_by_id(doc_id):
    """Retrieves the full text content of a document given its ID (filename)."""
    documents_folder = app_config['document_loading']['documents_folder']
    filepath = os.path.join(documents_folder, doc_id)
    if not os.path.exists(filepath):
        logger.error(f"Document file '{filepath}' not found.")
        return None
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        logger.error(f"Error reading document file {filepath}: {e}")
        return None

# --- 3. Perform text-based search ---
def search_text(query_text, k):
    """
    Performs a text-based similarity search using FAISS and Gemini embeddings.
    Returns a list of dictionaries with document_id, content, and distance.
    """
    if faiss_index is None or not faiss_id_to_doc_id_map:
        raise RuntimeError("Search system not fully initialized (index or mapping missing).")

    embedding_model = app_config['api_settings']['gemini_embedding_model']
    try:
        logger.info(f"Generating embedding for query: '{query_text}'")
        query_response = genai.embed_content(model=embedding_model, content=[query_text])
        query_embedding = np.array(query_response['embedding'], dtype='float32')
    except Exception as e:
        logger.error(f"Error generating query embedding with Gemini API: {e}")
        raise

    distances, indices = faiss_index.search(query_embedding, k)

    results = []
    for i, faiss_idx in enumerate(indices[0]):
        if 0 <= faiss_idx < len(faiss_id_to_doc_id_map):
            doc_id = faiss_id_to_doc_id_map[faiss_idx]
            document_content = get_document_content_by_id(doc_id) # Retrieve content on demand
            if document_content:
                results.append({
                    "document_id": doc_id,
                    "document_content": document_content,
                    "distance": float(distances[0][i])
                })
            else:
                logger.warning(f"Could not retrieve content for document ID: {doc_id}")
        else:
            logger.warning(f"Invalid FAISS index {faiss_idx} returned. Mapping might be stale.")
    return results

# --- Function to Generate Context for LLM ---
def generate_llm_context(search_results):
    """
    Compiles relevant content from search results into a single context string for the LLM.
    Truncates content if it exceeds max_length from config.
    """
    max_length = app_config['search_settings'].get('max_context_length', 4000)
    context = ""
    for i, result in enumerate(search_results):
        doc_id = result['document_id']
        content = result['document_content']
        
        doc_header = f"\n--- Document {i+1}: {doc_id} ---\n"
        
        remaining_length = max_length - len(context) - len(doc_header)
        
        if remaining_length <= 0:
            logger.warning(f"Max context length reached. Truncating context. Dropping document {doc_id}.")
            break

        if len(content) > remaining_length:
            content_to_add = content[:remaining_length] + "\n... [truncated] ...\n"
            logger.warning(f"Document {doc_id} content truncated to fit context.")
        else:
            content_to_add = content
        
        context += doc_header + content_to_add
        
    return context.strip()

# --- Function to Query LLM with RAG Context ---
def query_llm_with_rag(user_query, context):
    """
    Constructs an augmented prompt using the loaded template and queries the Gemini LLM.
    """
    if prompt_template is None:
        raise RuntimeError("Prompt template not loaded. Cannot query LLM effectively.")
    if llm_model is None:
        raise RuntimeError("LLM model not initialized.")

    final_prompt = prompt_template.format(context=context, question=user_query)
    
    logger.info("Querying LLM with RAG context.")

    try:
        response = llm_model.generate_content(final_prompt)
        generated_text = ""
        for part in response.parts:
            if hasattr(part, 'text'):
                generated_text += part.text
        return generated_text.strip()
    except Exception as e:
        logger.error(f"Error querying LLM: {e}")
        # Return a user-friendly error message, but log the full exception
        return "An internal error occurred while generating a response from the LLM."

# --- API Endpoints ---

@app.route('/api/health', methods=['GET'])
def health_check():
    """
    Performs a health check on the service, verifying all components are initialized.
    Returns the health status, model name, and timestamp.
    """
    # Service checkpoints
    is_healthy = all([
        app_config is not None,
        faiss_index is not None,
        faiss_id_to_doc_id_map,  # Check if list is populated
        prompt_template is not None,
        llm_model is not None
    ])

    status = "healthy" if is_healthy else "unhealthy"
    status_code = 200 if is_healthy else 503

    model_name = "unknown"
    if app_config and 'api_settings' in app_config and 'gemini_llm_model' in app_config['api_settings']:
        model_name = app_config['api_settings']['gemini_llm_model']

    timestamp = datetime.now(timezone.utc).isoformat(timespec='milliseconds').replace('+00:00', 'Z')

    response = {
        "status": status,
        "model": model_name,
        "timestamp": timestamp
    }

    return jsonify(response), status_code

@app.route('/api/chat', methods=['POST'])
def chat_api():
    """
    RESTful API endpoint for RAG-powered chat.
    Expects a JSON payload with 'current_message' (object with role and content) 
    and optional 'chat_history' (array of message objects).
    """
    data = request.get_json()
    if not data or 'current_message' not in data:
        return jsonify({"error": "Missing 'current_message' in request body."}), 400

    current_message = data['current_message']
    chat_history = data.get('chat_history', [])
    k = data.get('k', app_config['search_settings']['default_k_neighbors'])

    # Validate current_message structure
    if not isinstance(current_message, dict) or 'role' not in current_message or 'content' not in current_message:
        return jsonify({"error": "current_message must be an object with 'role' and 'content' fields."}), 400
    
    if current_message['role'] != 'user':
        return jsonify({"error": "current_message role must be 'user'."}), 400
    
    user_query = current_message['content']
    if not isinstance(user_query, str) or not user_query.strip():
        return jsonify({"error": "User message content must be a non-empty string."}), 400

    # Validate chat_history structure
    if not isinstance(chat_history, list):
        return jsonify({"error": "chat_history must be an array."}), 400
    
    for msg in chat_history:
        if not isinstance(msg, dict) or 'role' not in msg or 'content' not in msg:
            return jsonify({"error": "Each message in chat_history must have 'role' and 'content' fields."}), 400
        if msg['role'] not in ['user', 'assistant']:
            return jsonify({"error": "Message roles must be either 'user' or 'assistant'."}), 400

    if not isinstance(k, int) or k <= 0:
        return jsonify({"error": "k must be a positive integer."}), 400

    try:
        logger.info(f"API Request: Query='{user_query}', k={k}, Chat history length={len(chat_history)}")
        
        retrieved_results = search_text(user_query, k)
        context = generate_llm_context(retrieved_results)
        llm_response = query_llm_with_rag(user_query, context)

        # Create updated chat history with the current user message
        updated_chat_history = chat_history + [current_message]
        
        # Create current message with assistant response
        current_message = {
            "role": "assistant",
            "content": llm_response
        }

        response = {
            "current_message": current_message,
            "chat_history": updated_chat_history
        }

        return jsonify(response), 200

    except FileNotFoundError as e:
        logger.exception("File not found error during API processing:")
        return jsonify({"error": f"Server initialization error: {e}. Missing required files."}), 500
    except ValueError as e:
        logger.exception("Value error during API processing:")
        return jsonify({"error": f"Configuration error: {e}. Check API key."}), 500
    except RuntimeError as e:
        logger.exception("Runtime error during API processing:")
        return jsonify({"error": f"Application initialization error: {e}. Please check server logs."}), 500
    except Exception as e:
        logger.exception("An unexpected error occurred during API processing:")
        return jsonify({"error": f"An unexpected server error occurred: {str(e)}"}), 500

# --- App Initialization on Startup ---
# This block runs once when the Flask application starts
with app.app_context():
    try:
        # Load config first to set up logging
        temp_config_path = "config.json"
        temp_config = {}
        try:
            with open(temp_config_path, 'r', encoding='utf-8') as f:
                temp_config = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            logger.critical("Failed to load config.json at startup. Cannot proceed.")
            exit(1)

        # Configure logging based on loaded config
        log_level = logging.INFO if temp_config.get('application', {}).get('enable_logging', True) else logging.CRITICAL
        logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')
        
        # Now perform the full load
        app_config = load_config() # This will reload, but now logging is set

        logger.info(f"Initializing {app_config['application']['app_name']} API...")

        configure_gemini(
            app_config['api_settings']['gemini_api_key_env_var'],
            app_config['api_settings']['gemini_embedding_model'],
            app_config['api_settings']['gemini_llm_model']
        )
        
        prompt_template = load_prompt_template(app_config['application']['prompt_template_file'])
        
        load_faiss_artifacts(
            app_config['faiss_index_settings']['index_file_name'],
            app_config['faiss_index_settings']['mapping_file_name']
        )
        logger.info("API Initialization complete.")
    except Exception as e:
        logger.critical(f"FATAL ERROR during API initialization: {e}", exc_info=True)
        # In a production setup, you might want to exit or fail health checks here.
        # For development, just log and let Flask run, but requests will fail.
        faiss_index = None # Ensure a state that will fail requests

# --- Run the Flask App ---
if __name__ == '__main__':
    # Use 0.0.0.0 to make it accessible from other machines on the network
    # In production, use a WSGI server like Gunicorn
    app.run(debug=True, host='0.0.0.0', port=1717)