---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🖼️ Segmentation
Header 3: Train
---
YOLOv5 segmentation training supports automatic download of the COCO128-seg dataset via the `--data coco128-seg.yaml` argument. For the full COCO-segments dataset, download it manually using `bash data/scripts/get_coco.sh --train --val --segments` and then train with `python train.py --data coco.yaml`.  
```bash
# Train on a single GPU
python segment/train.py --data coco128-seg.yaml --weights yolov5s-seg.pt --img 640

# Train using Multi-GPU Distributed Data Parallel (DDP)
python -m torch.distributed.run --nproc_per_node 4 --master_port 1 segment/train.py --data coco128-seg.yaml --weights yolov5s-seg.pt --img 640 --device 0,1,2,3
```