---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 🏷️ Classification
---
YOLOv5 release v6.2 introduced support for image classification model training, validation, and deployment. Check the Release Notes for details and the YOLOv5 Classification Colab Notebook for quickstart guides.  

Classification Checkpoints  
  
YOLOv5-cls classification models were trained on ImageNet for 90 epochs using a 4xA100 instance. ResNet and EfficientNet models were trained alongside under identical settings for comparison. Models were exported to ONNX FP32 (CPU speed tests) and TensorRT FP16 (GPU speed tests). All speed tests were run on Google Colab Pro for reproducibility.  
| Model                                                                                              | Size(pixels) | Acctop1 | Acctop5 | Training90 epochs4xA100 (hours) | SpeedONNX CPU(ms) | SpeedTensorRT V100(ms) | Params(M) | FLOPs@224 (B) |
| -------------------------------------------------------------------------------------------------- | --------------------- | ---------------- | ---------------- | -------------------------------------------- | ------------------------------ | ----------------------------------- | ------------------ | ---------------------- |
| YOLOv5n-cls         | 224                   | 64.6             | 85.4             | 7:59                                         | **3.3**                        | **0.5**                             | **2.5**            | **0.5**                |
| YOLOv5s-cls         | 224                   | 71.5             | 90.2             | 8:09                                         | 6.6                            | 0.6                                 | 5.4                | 1.4                    |
| YOLOv5m-cls         | 224                   | 75.9             | 92.9             | 10:06                                        | 15.5                           | 0.9                                 | 12.9               | 3.9                    |
| YOLOv5l-cls         | 224                   | 78.0             | 94.0             | 11:56                                        | 26.9                           | 1.4                                 | 26.5               | 8.5                    |
| YOLOv5x-cls         | 224                   | **79.0**         | **94.4**         | 15:04                                        | 54.3                           | 1.8                                 | 48.1               | 15.9                   |
|                                                                                                    |                       |                  |                  |                                              |                                |                                     |                    |                        |
| ResNet18               | 224                   | 70.3             | 89.5             | **6:47**                                     | 11.2                           | 0.5                                 | 11.7               | 3.7                    |
| ResNet34               | 224                   | 73.9             | 91.8             | 8:33                                         | 20.6                           | 0.9                                 | 21.8               | 7.4                    |
| ResNet50               | 224                   | 76.8             | 93.4             | 11:10                                        | 23.4                           | 1.0                                 | 25.6               | 8.5                    |
| ResNet101             | 224                   | 78.5             | 94.3             | 17:10                                        | 42.1                           | 1.9                                 | 44.5               | 15.9                   |
|                                                                                                    |                       |                  |                  |                                              |                                |                                     |                    |                        |
| EfficientNet_b0 | 224                   | 75.1             | 92.4             | 13:03                                        | 12.5                           | 1.3                                 | 5.3                | 1.0                    |
| EfficientNet_b1 | 224                   | 76.4             | 93.2             | 17:04                                        | 14.9                           | 1.6                                 | 7.8                | 1.5                    |
| EfficientNet_b2 | 224                   | 76.6             | 93.4             | 17:10                                        | 15.9                           | 1.6                                 | 9.1                | 1.7                    |
| EfficientNet_b3 | 224                   | 77.7             | 94.0             | 19:19                                        | 18.9                           | 1.9                                 | 12.2               | 2.4                    |  

Table Notes (click to expand)  
- All checkpoints were trained for 90 epochs using the SGD optimizer with `lr0=0.001` and `weight_decay=5e-5` at an image size of 224 pixels, using default settings.Training runs are logged at 
- **Accuracy** values (top-1 and top-5) represent single-model, single-scale performance on the ImageNet-1k dataset.Reproduce using: `python classify/val.py --data ../datasets/imagenet --img 224`
- **Speed** metrics are averaged over 100 inference images using a Google Colab Pro V100 High-RAM instance.Reproduce using: `python classify/val.py --data ../datasets/imagenet --img 224 --batch 1`
- **Export** to ONNX (FP32) and TensorRT (FP16) was performed using `export.py`.Reproduce using: `python export.py --weights yolov5s-cls.pt --include engine onnx --imgsz 224`  

  

Classification Usage Examples &nbsp;