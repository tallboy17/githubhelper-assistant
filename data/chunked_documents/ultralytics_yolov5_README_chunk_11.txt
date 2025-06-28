---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🖼️ Segmentation
Header 3: Predict
---
Use the pretrained YOLOv5m-seg.pt model to perform segmentation on `bus.jpg`:  
```bash
# Run prediction
python segment/predict.py --weights yolov5m-seg.pt --source data/images/bus.jpg
```  
```python
# Load model from PyTorch Hub (Note: Inference support might vary)
model = torch.hub.load("ultralytics/yolov5", "custom", "yolov5m-seg.pt")
```  
| !Zidane Segmentation Example | !Bus Segmentation Example |
| :-----------------------------------------------------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------------------------------------------------: |