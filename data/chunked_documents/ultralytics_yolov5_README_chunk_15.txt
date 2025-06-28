---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🏷️ Classification
Header 3: Val
---
Validate the accuracy of the YOLOv5m-cls model on the ImageNet-1k validation dataset:  
```bash
# Download ImageNet validation split (6.3GB, 50,000 images)
bash data/scripts/get_imagenet.sh --val

# Validate the model
python classify/val.py --weights yolov5m-cls.pt --data ../datasets/imagenet --img 224
```