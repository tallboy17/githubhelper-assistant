---
repo: PaddlePaddle/PaddleOCR
readme_filename: PaddlePaddle_PaddleOCR_README.md
stars: 51003
forks: 8373
watchers: 51003
contributors_count: 245
license: Apache-2.0
Header 2: ⚡ Quick Start
Header 3: 4. Run inference by API
---
**4.1 PP-OCRv5 Example**
```python
# Initialize PaddleOCR instance
from paddleocr import PaddleOCR
ocr = PaddleOCR(
use_doc_orientation_classify=False,
use_doc_unwarping=False,
use_textline_orientation=False)

# Run OCR inference on a sample image
result = ocr.predict(
input="

# Visualize the results and save the JSON results
for res in result:
res.print()
res.save_to_img("output")
res.save_to_json("output")
```  

4.2 PP-StructureV3 Example  
```python
from pathlib import Path
from paddleocr import PPStructureV3

pipeline = PPStructureV3(
use_doc_orientation_classify=False,
use_doc_unwarping=False
)

# For Image
output = pipeline.predict(
input="
)

# Visualize the results and save the JSON results
for res in output:
res.print()
res.save_to_json(save_path="output")
res.save_to_markdown(save_path="output")
```  
  

4.3 PP-ChatOCRv4 Example  
```python
from paddleocr import PPChatOCRv4Doc

chat_bot_config = {
"module_name": "chat_bot",
"model_name": "ernie-3.5-8k",
"base_url": "
"api_type": "openai",
"api_key": "api_key",  # your api_key
}

retriever_config = {
"module_name": "retriever",
"model_name": "embedding-v1",
"base_url": "
"api_type": "qianfan",
"api_key": "api_key",  # your api_key
}

pipeline = PPChatOCRv4Doc(
use_doc_orientation_classify=False,
use_doc_unwarping=False
)

visual_predict_res = pipeline.visual_predict(
input="
use_common_ocr=True,
use_seal_recognition=True,
use_table_recognition=True,
)

mllm_predict_info = None
use_mllm = False
# If a multimodal large model is used, the local mllm service needs to be started. You can refer to the documentation:  performs deployment and updates the mllm_chat_bot_config configuration.
if use_mllm:
mllm_chat_bot_config = {
"module_name": "chat_bot",
"model_name": "PP-DocBee",
"base_url": "  # your local mllm service url
"api_type": "openai",
"api_key": "api_key",  # your api_key
}

mllm_predict_res = pipeline.mllm_pred(
input="
key_list=["驾驶室准乘人数"],
mllm_chat_bot_config=mllm_chat_bot_config,
)
mllm_predict_info = mllm_predict_res["mllm_res"]

visual_info_list = []
for res in visual_predict_res:
visual_info_list.append(res["visual_info"])
layout_parsing_result = res["layout_parsing_result"]

vector_info = pipeline.build_vector(
visual_info_list, flag_save_bytes_vector=True, retriever_config=retriever_config
)
chat_result = pipeline.chat(
key_list=["驾驶室准乘人数"],
visual_info=visual_info_list,
vector_info=vector_info,
mllm_predict_info=mllm_predict_info,
chat_bot_config=chat_bot_config,
retriever_config=retriever_config,
)
print(chat_result)
```  
