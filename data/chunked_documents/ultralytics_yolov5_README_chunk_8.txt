---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🖼️ Segmentation
---
The YOLOv5 release v7.0 introduced instance segmentation models that achieve state-of-the-art performance. These models are designed for easy training, validation, and deployment. For full details, see the Release Notes and explore the YOLOv5 Segmentation Colab Notebook for quickstart examples.  

Segmentation Checkpoints  



  
YOLOv5 segmentation models were trained on the COCO dataset for 300 epochs at an image size of 640 pixels using A100 GPUs. Models were exported to ONNX FP32 for CPU speed tests and TensorRT FP16 for GPU speed tests. All speed tests were conducted on Google Colab Pro notebooks for reproducibility.  
| Model                                                                                      | Size(pixels) | mAPbox50-95 | mAPmask50-95 | Train Time300 epochsA100 (hours) | SpeedONNX CPU(ms) | SpeedTRT A100(ms) | Params(M) | FLOPs@640 (B) |
| ------------------------------------------------------------------------------------------ | --------------------- | -------------------- | --------------------- | --------------------------------------------- | ------------------------------ | ------------------------------ | ------------------ | ---------------------- |
| YOLOv5n-seg | 640                   | 27.6                 | 23.4                  | 80:17                                         | **62.7**                       | **1.2**                        | **2.0**            | **7.1**                |
| YOLOv5s-seg | 640                   | 37.6                 | 31.7                  | 88:16                                         | 173.3                          | 1.4                            | 7.6                | 26.4                   |
| YOLOv5m-seg | 640                   | 45.0                 | 37.1                  | 108:36                                        | 427.0                          | 2.2                            | 22.0               | 70.8                   |
| YOLOv5l-seg | 640                   | 49.0                 | 39.9                  | 66:43 (2x)                                    | 857.4                          | 2.9                            | 47.9               | 147.7                  |
| YOLOv5x-seg | 640                   | **50.7**             | **41.4**              | 62:56 (3x)                                    | 1579.2                         | 4.5                            | 88.8               | 265.7                  |  
- All checkpoints were trained for 300 epochs using the SGD optimizer with `lr0=0.01` and `weight_decay=5e-5` at an image size of 640 pixels, using default settings.Training runs are logged at 
- **Accuracy** values represent single-model, single-scale performance on the COCO dataset.Reproduce using: `python segment/val.py --data coco.yaml --weights yolov5s-seg.pt`
- **Speed** metrics are averaged over 100 inference images using a Colab Pro A100 High-RAM instance. Values indicate inference speed only (NMS adds approximately 1ms per image).Reproduce using: `python segment/val.py --data coco.yaml --weights yolov5s-seg.pt --batch 1`
- **Export** to ONNX (FP32) and TensorRT (FP16) was performed using `export.py`.Reproduce using: `python export.py --weights yolov5s-seg.pt --include engine --device 0 --half`  
  

Segmentation Usage Examples &nbsp;