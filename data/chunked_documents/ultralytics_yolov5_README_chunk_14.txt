---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🏷️ Classification
Header 3: Train
---
YOLOv5 classification training supports automatic download for datasets like MNIST, Fashion-MNIST, CIFAR10, CIFAR100, Imagenette, Imagewoof, and ImageNet using the `--data` argument. For example, start training on MNIST with `--data mnist`.  
```bash
# Train on a single GPU using CIFAR-100 dataset
python classify/train.py --model yolov5s-cls.pt --data cifar100 --epochs 5 --img 224 --batch 128

# Train using Multi-GPU DDP on ImageNet dataset
python -m torch.distributed.run --nproc_per_node 4 --master_port 1 classify/train.py --model yolov5s-cls.pt --data imagenet --epochs 5 --img 224 --device 0,1,2,3
```