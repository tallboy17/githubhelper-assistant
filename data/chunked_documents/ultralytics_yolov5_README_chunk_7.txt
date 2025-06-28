---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🤔 Why YOLOv5?
Header 3: Pretrained Checkpoints
---
This table shows the performance metrics for various YOLOv5 models trained on the COCO dataset.  
| Model                                                                                                                                                                    | Size(pixels) | mAPval50-95 | mAPval50 | SpeedCPU b1(ms) | SpeedV100 b1(ms) | SpeedV100 b32(ms) | Params(M) | FLOPs@640 (B) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- | -------------------- | ----------------- | ---------------------------- | ----------------------------- | ------------------------------ | ------------------ | ---------------------- |
| YOLOv5n                                                                                       | 640                   | 28.0                 | 45.7              | **45**                       | **6.3**                       | **0.6**                        | **1.9**            | **4.5**                |
| YOLOv5s                                                                                       | 640                   | 37.4                 | 56.8              | 98                           | 6.4                           | 0.9                            | 7.2                | 16.5                   |
| YOLOv5m                                                                                       | 640                   | 45.4                 | 64.1              | 224                          | 8.2                           | 1.7                            | 21.2               | 49.0                   |
| YOLOv5l                                                                                       | 640                   | 49.0                 | 67.3              | 430                          | 10.1                          | 2.7                            | 46.5               | 109.1                  |
| YOLOv5x                                                                                       | 640                   | 50.7                 | 68.9              | 766                          | 12.1                          | 4.8                            | 86.7               | 205.7                  |
|                                                                                                                                                                          |                       |                      |                   |                              |                               |                                |                    |                        |
| YOLOv5n6                                                                                     | 1280                  | 36.0                 | 54.4              | 153                          | 8.1                           | 2.1                            | 3.2                | 4.6                    |
| YOLOv5s6                                                                                     | 1280                  | 44.8                 | 63.7              | 385                          | 8.2                           | 3.6                            | 12.6               | 16.8                   |
| YOLOv5m6                                                                                     | 1280                  | 51.3                 | 69.3              | 887                          | 11.1                          | 6.8                            | 35.7               | 50.0                   |
| YOLOv5l6                                                                                     | 1280                  | 53.7                 | 71.3              | 1784                         | 15.8                          | 10.5                           | 76.8               | 111.4                  |
| YOLOv5x6+ [[TTA]]( | 12801536          | 55.0**55.8**     | 72.7**72.7**  | 3136-                    | 26.2-                     | 19.4-                      | 140.7-         | 209.8-             |  

Table Notes  
- All checkpoints were trained for 300 epochs using default settings. Nano (n) and Small (s) models use hyp.scratch-low.yaml hyperparameters, while Medium (m), Large (l), and Extra-Large (x) models use hyp.scratch-high.yaml.
- **mAPval** values represent single-model, single-scale performance on the COCO val2017 dataset.Reproduce using: `python val.py --data coco.yaml --img 640 --conf 0.001 --iou 0.65`
- **Speed** metrics are averaged over COCO val images using an AWS p3.2xlarge V100 instance. Non-Maximum Suppression (NMS) time (~1 ms/image) is not included.Reproduce using: `python val.py --data coco.yaml --img 640 --task speed --batch 1`
- **TTA** (Test Time Augmentation) includes reflection and scale augmentations for improved accuracy.Reproduce using: `python val.py --data coco.yaml --img 1536 --iou 0.7 --augment`  
