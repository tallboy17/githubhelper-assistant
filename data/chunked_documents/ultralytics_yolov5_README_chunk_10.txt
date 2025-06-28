---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🖼️ Segmentation
Header 3: Val
---
Validate the mask mean Average Precision (mAP) of YOLOv5s-seg on the COCO dataset:  
```bash
# Download COCO validation segments split (780MB, 5000 images)
bash data/scripts/get_coco.sh --val --segments

# Validate the model
python segment/val.py --weights yolov5s-seg.pt --data coco.yaml --img 640
```