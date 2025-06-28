---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🤔 Why YOLOv5?
---
YOLOv5 is designed for simplicity and ease of use. We prioritize real-world performance and accessibility.  


YOLOv5-P5 640 Figure  



Figure Notes  
- **COCO AP val** denotes the mean Average Precision (mAP) at Intersection over Union (IoU) thresholds from 0.5 to 0.95, measured on the 5,000-image COCO val2017 dataset across various inference sizes (256 to 1536 pixels).
- **GPU Speed** measures the average inference time per image on the COCO val2017 dataset using an AWS p3.2xlarge V100 instance with a batch size of 32.
- **EfficientDet** data is sourced from the google/automl repository at batch size 8.
- **Reproduce** these results using the command: `python val.py --task study --data coco.yaml --iou 0.7 --weights yolov5n6.pt yolov5s6.pt yolov5m6.pt yolov5l6.pt yolov5x6.pt`  
