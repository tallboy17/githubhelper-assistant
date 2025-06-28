---
repo: PaddlePaddle/PaddleOCR
readme_filename: PaddlePaddle_PaddleOCR_README.md
stars: 51003
forks: 8373
watchers: 51003
contributors_count: 245
license: Apache-2.0
Header 2: ⚡ Quick Start
Header 3: 3. Run inference by CLI
---
```bash
# Run PP-OCRv5 inference
paddleocr ocr -i  --use_doc_orientation_classify False --use_doc_unwarping False --use_textline_orientation False

# Run PP-StructureV3 inference
paddleocr pp_structurev3 -i  --use_doc_orientation_classify False --use_doc_unwarping False

# Get the Qianfan API Key at first, and then run PP-ChatOCRv4 inference
paddleocr pp_chatocrv4_doc -i  -k 驾驶室准乘人数 --qianfan_api_key your_api_key --use_doc_orientation_classify False --use_doc_unwarping False

# Get more information about "paddleocr ocr"
paddleocr ocr --help
```