---
repo: PaddlePaddle/PaddleOCR
readme_filename: PaddlePaddle_PaddleOCR_README.md
stars: 51003
forks: 8373
watchers: 51003
contributors_count: 245
license: Apache-2.0
Header 2: 📣 Recent updates
---
#### **2025.06.26: Release of PaddleOCR 3.0.3**, includes:
- Bug Fix: Resolved the issue where the `enable_mkldnn` parameter was not effective, restoring the default behavior of using MKL-DNN for CPU inference.  
#### 🔥🔥 **2025.06.19: Release of PaddleOCR 3.0.2**, includes:  
- **New Features:**  
- The default download source has been changed from `BOS` to `HuggingFace`. Users can also change the environment variable `PADDLE_PDX_MODEL_SOURCE` to `BOS` to set the model download source back to Baidu Object Storage (BOS).
- Added service invocation examples for six languages—C++, Java, Go, C#, Node.js, and PHP—for pipelines like PP-OCRv5, PP-StructureV3, and PP-ChatOCRv4.
- Improved the layout partition sorting algorithm in the PP-StructureV3 pipeline, enhancing the sorting logic for complex vertical layouts to deliver better results.
- Enhanced model selection logic: when a language is specified but a model version is not, the system will automatically select the latest model version supporting that language.
- Set a default upper limit for MKL-DNN cache size to prevent unlimited growth, while also allowing users to configure cache capacity.
- Updated default configurations for high-performance inference to support Paddle MKL-DNN acceleration and optimized the logic for automatic configuration selection for smarter choices.
- Adjusted the logic for obtaining the default device to consider the actual support for computing devices by the installed Paddle framework, making program behavior more intuitive.
- Added Android example for PP-OCRv5. Details.  
- **Bug Fixes:**  
- Fixed an issue with some CLI parameters in PP-StructureV3 not taking effect.
- Resolved an issue where `export_paddlex_config_to_yaml` would not function correctly in certain cases.
- Corrected the discrepancy between the actual behavior of `save_path` and its documentation description.
- Fixed potential multithreading errors when using MKL-DNN in basic service deployment.
- Corrected channel order errors in image preprocessing for the Latex-OCR model.
- Fixed channel order errors in saving visualized images within the text recognition module.
- Resolved channel order errors in visualized table results within PP-StructureV3 pipeline.
- Fixed an overflow issue in the calculation of `overlap_ratio` under extremely special circumstances in the PP-StructureV3 pipeline.  
- **Documentation Improvements:**  
- Updated the description of the `enable_mkldnn` parameter in the documentation to accurately reflect the program's actual behavior.
- Fixed errors in the documentation regarding the `lang` and `ocr_version` parameters.
- Added instructions for exporting production line configuration files via CLI.
- Fixed missing columns in the performance data table for PP-OCRv5.
- Refined benchmark metrics for PP-StructureV3 across different configurations.  
- **Others:**  
- Relaxed version restrictions on dependencies like numpy and pandas, restoring support for Python 3.12.  

History Log  
#### **🔥🔥 2025.06.05: Release of PaddleOCR 3.0.1, includes:**  
- **Optimisation of certain models and model configurations:**
- Updated the default model configuration for PP-OCRv5, changing both detection and recognition from mobile to server models. To improve default performance in most scenarios, the parameter `limit_side_len` in the configuration has been changed from 736 to 64.
- Added a new text line orientation classification model `PP-LCNet_x1_0_textline_ori` with an accuracy of 99.42%. The default text line orientation classifier for OCR, PP-StructureV3, and PP-ChatOCRv4 pipelines has been updated to this model.
- Optimised the text line orientation classification model `PP-LCNet_x0_25_textline_ori`, improving accuracy by 3.3 percentage points to a current accuracy of 98.85%.  
- **Optimizations and fixes for some issues in version 3.0.0, details**  
🔥🔥2025.05.20: Official Release of **PaddleOCR v3.0**, including:
- **PP-OCRv5**: High-Accuracy Text Recognition Model for All Scenarios - Instant Text from Images/PDFs.
1. 🌐 Single-model support for **five** text types - Seamlessly process **Simplified Chinese, Traditional Chinese, Simplified Chinese Pinyin, English** and **Japanese** within a single model.
2. ✍️ Improved **handwriting recognition**: Significantly better at complex cursive scripts and non-standard handwriting.
3. 🎯 **13-point accuracy gain** over PP-OCRv4, achieving state-of-the-art performance across a variety of real-world scenarios.  
- **PP-StructureV3**: General-Purpose Document Parsing – Unleash SOTA Images/PDFs Parsing for Real-World Scenarios!
1. 🧮 **High-Accuracy multi-scene PDF parsing**, leading both open- and closed-source solutions on the OmniDocBench benchmark.
2. 🧠 Specialized capabilities include **seal recognition**, **chart-to-table conversion**, **table recognition with nested formulas/images**, **vertical text document parsing**, and **complex table structure analysis**.  
- **PP-ChatOCRv4**: Intelligent Document Understanding – Extract Key Information, not just text from Images/PDFs.
1. 🔥 **15-point accuracy gain** in key-information extraction on PDF/PNG/JPG files over the previous generation.
2. 💻 Native support for **ERNIE 4.5 Turbo**, with compatibility for large-model deployments via PaddleNLP, Ollama, vLLM, and more.
3. 🤝 Integrated PP-DocBee2, enabling extraction and understanding of printed text, handwriting, seals, tables, charts, and other common elements in complex documents.  
History Log  
