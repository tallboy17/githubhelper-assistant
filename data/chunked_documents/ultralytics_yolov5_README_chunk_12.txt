---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🖼️ Segmentation
Header 3: Export
---
Export the YOLOv5s-seg model to ONNX and TensorRT formats:  
```bash
# Export model
python export.py --weights yolov5s-seg.pt --include onnx engine --img 640 --device 0
```  
