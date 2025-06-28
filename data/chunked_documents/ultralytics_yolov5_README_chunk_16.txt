---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🏷️ Classification
Header 3: Predict
---
Use the pretrained YOLOv5s-cls.pt model to classify the image `bus.jpg`:  
```bash
# Run prediction
python classify/predict.py --weights yolov5s-cls.pt --source data/images/bus.jpg
```  
```python
# Load model from PyTorch Hub
model = torch.hub.load("ultralytics/yolov5", "custom", "yolov5s-cls.pt")
```