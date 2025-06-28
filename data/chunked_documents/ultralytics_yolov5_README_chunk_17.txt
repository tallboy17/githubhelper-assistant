---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🏷️ Classification
Header 3: Export
---
Export trained YOLOv5s-cls, ResNet50, and EfficientNet_b0 models to ONNX and TensorRT formats:  
```bash
# Export models
python export.py --weights yolov5s-cls.pt resnet50.pt efficientnet_b0.pt --include onnx engine --img 224
```  
