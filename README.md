# GitHub Helper AI

A powerful Retrieval-Augmented Generation (RAG) API that helps users discover and get recommendations for relevant GitHub repositories based on their queries. Built with Flask, Google Gemini AI, and FAISS for efficient similarity search.

## 🚀 Features

- **Intelligent Repository Discovery**: Uses AI to analyze and recommend GitHub repositories based on user queries
- **RAG-Powered Responses**: Combines retrieval and generation for accurate, context-aware recommendations
- **Fast Similarity Search**: FAISS-based vector search for quick document retrieval
- **RESTful API**: Clean, well-documented API endpoints for easy integration
- **Production Ready**: Configurable for both development and production environments

## 📋 Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- FAISS index files (generated from your GitHub repository data)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd githubhelper-assistant
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Google Gemini API key**:
   ```bash
   export GEMINI_API_KEY="your_gemini_api_key_here"
   ```

4. **Configure the application**:
   - Update `config.json` with your specific paths and settings
   - Ensure your FAISS index files are in the correct location
   - Place your GitHub repository documents in the specified documents folder

## ⚙️ Configuration

The application uses `config.json` for configuration. Key settings include:

```json
{
    "api_settings": {
        "gemini_api_key_env_var": "GEMINI_API_KEY",
        "gemini_embedding_model": "models/embedding-001",
        "gemini_llm_model": "gemini-2.0-flash"
    },
    "document_loading": {
        "documents_folder": "/disk/github_chunks",
        "allowed_file_extensions": [".txt", ".md"]
    },
    "faiss_index_settings": {
        "index_file_name": "/disk/indexes/index.faiss",
        "mapping_file_name": "/disk/indexes/faiss_id_to_doc_id_map.json"
    },
    "search_settings": {
        "default_k_neighbors": 5,
        "max_context_length": 5000
    }
}
```

## 🚀 Running the Application

### Development Mode

```bash
python github_helper_ai.py
```

The application will start on `http://localhost:1717`

**Note**: You'll see a warning about the development server. This is normal for development. For production, use a WSGI server like Gunicorn.

### Production Mode

For production deployment, use a WSGI server like Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:1717 github_helper_ai:app
```

## 🚀 API Endpoints

### Health Check
```http
GET /api/health
```

Returns the health status of the service:
```json
{
    "status": "healthy",
    "model": "gemini-2.0-flash",
    "timestamp": "2024-01-01T12:00:00.000Z"
}
```

### Chat API
```http
POST /api/chat
```

**Request Body**:
```json
{
    "current_message": {
        "role": "user",
        "content": "I'm looking for Python machine learning libraries"
    },
    "chat_history": [],
    "k": 5
}
```

**Response**:
```json
{
    "current_message": {
        "role": "assistant",
        "content": "Based on your query, here are some relevant GitHub repositories..."
    },
    "chat_history": [
        {
            "role": "user",
            "content": "I'm looking for Python machine learning libraries"
        }
    ]
}
```

## 🔧 Project Structure

```
githubhelper-assistant/
├── github_helper_ai.py      # Main Flask application
├── config.json             # Configuration file
├── prompt_template.txt     # AI prompt template
├── requirements.txt        # Python dependencies
├── data/
│   ├── indexes/           # FAISS index files
│   └── chunked_documents/ # GitHub repository documents
└── README.md
```

## 🧠 How It Works

1. **Document Indexing**: GitHub repository information is processed and indexed using FAISS for fast similarity search
2. **Query Processing**: User queries are converted to embeddings using Google's Gemini embedding model
3. **Retrieval**: FAISS performs similarity search to find the most relevant repository documents
4. **Generation**: The retrieved context is combined with the user query and sent to Gemini LLM for generating recommendations
5. **Response**: The AI provides personalized GitHub repository recommendations with explanations

## 🔒 Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key (required)

## 🐛 Troubleshooting

### Common Issues

1. **Missing FAISS Index Files**: Ensure your index files are generated and placed in the correct location
2. **API Key Issues**: Verify your Gemini API key is set correctly
3. **Port Already in Use**: Change the port in the configuration or stop other services using port 1717
4. **Development Server Warning**: This is normal for development. Use Gunicorn for production.

### Health Check

Use the `/api/health` endpoint to verify all components are properly initialized.

## 🔒 Important Notes

- **Development vs Production**: The Flask development server is fine for local development but use Gunicorn for production
- **API Key Security**: Never commit your API key to version control. Use environment variables
- **File Paths**: Update the document and index file paths in `config.json` to match your setup
- **Memory Requirements**: FAISS indexes can be memory-intensive. Ensure adequate RAM for your dataset size

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

[Add your license information here]

## 🤝 Acknowledgments

- Google Gemini AI for the language model and embeddings
- FAISS for efficient similarity search
- Flask for the web framework

## 📞 Support

For issues and questions, please open an issue in the repository or contact [your contact information].
