---
repo: ultralytics/yolov5
readme_filename: ultralytics_yolov5_README.md
stars: 54363
forks: 17014
watchers: 54363
contributors_count: 335
license: AGPL-3.0
Header 2: 📚 Documentation
---
See the YOLOv5 Docs for full documentation on training, testing, and deployment. See below for quickstart examples.  

Install  
Clone the repository and install dependencies in a **Python>=3.8.0** environment. Ensure you have **PyTorch>=1.8** installed.  
```bash
# Clone the YOLOv5 repository
git clone 

# Navigate to the cloned directory
cd yolov5

# Install required packages
pip install -r requirements.txt
```  
  

Inference with PyTorch Hub  
Use YOLOv5 via PyTorch Hub for inference. Models are automatically downloaded from the latest YOLOv5 release.  
```python
import torch

# Load a YOLOv5 model (options: yolov5n, yolov5s, yolov5m, yolov5l, yolov5x)
model = torch.hub.load("ultralytics/yolov5", "yolov5s")  # Default: yolov5s

# Define the input image source (URL, local file, PIL image, OpenCV frame, numpy array, or list)
img = "  # Example image

# Perform inference (handles batching, resizing, normalization automatically)
results = model(img)

# Process the results (options: .print(), .show(), .save(), .crop(), .pandas())
results.print()  # Print results to console
results.show()  # Display results in a window
results.save()  # Save results to runs/detect/exp
```  
  

Inference with detect.py  
The `detect.py` script runs inference on various sources. It automatically downloads models from the latest YOLOv5 release and saves the results to the `runs/detect` directory.  
```bash
# Run inference using a webcam
python detect.py --weights yolov5s.pt --source 0

# Run inference on a local image file
python detect.py --weights yolov5s.pt --source img.jpg

# Run inference on a local video file
python detect.py --weights yolov5s.pt --source vid.mp4

# Run inference on a screen capture
python detect.py --weights yolov5s.pt --source screen

# Run inference on a directory of images
python detect.py --weights yolov5s.pt --source path/to/images/

# Run inference on a text file listing image paths
python detect.py --weights yolov5s.pt --source list.txt

# Run inference on a text file listing stream URLs
python detect.py --weights yolov5s.pt --source list.streams

# Run inference using a glob pattern for images
python detect.py --weights yolov5s.pt --source 'path/to/*.jpg'

# Run inference on a YouTube video URL
python detect.py --weights yolov5s.pt --source '

# Run inference on an RTSP, RTMP, or HTTP stream
python detect.py --weights yolov5s.pt --source 'rtsp://example.com/media.mp4'
```  
  

Training  
The commands below demonstrate how to reproduce YOLOv5 COCO dataset results. Both models and datasets are downloaded automatically from the latest YOLOv5 release. Training times for YOLOv5n/s/m/l/x are approximately 1/2/4/6/8 days on a single NVIDIA V100 GPU. Using Multi-GPU training can significantly reduce training time. Use the largest `--batch-size` your hardware allows, or use `--batch-size -1` for YOLOv5 AutoBatch. The batch sizes shown below are for V100-16GB GPUs.  
```bash
# Train YOLOv5n on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5n.yaml --batch-size 128

# Train YOLOv5s on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5s.yaml --batch-size 64

# Train YOLOv5m on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5m.yaml --batch-size 40

# Train YOLOv5l on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5l.yaml --batch-size 24

# Train YOLOv5x on COCO for 300 epochs
python train.py --data coco.yaml --epochs 300 --weights '' --cfg yolov5x.yaml --batch-size 16
```  
  
  

Tutorials  
- **Train Custom Data** 🚀 **RECOMMENDED**: Learn how to train YOLOv5 on your own datasets.
- **Tips for Best Training Results** ☘️: Improve your model's performance with expert tips.
- **Multi-GPU Training**: Speed up training using multiple GPUs.
- **PyTorch Hub Integration** 🌟 **NEW**: Easily load models using PyTorch Hub.
- **Model Export (TFLite, ONNX, CoreML, TensorRT)** 🚀: Convert your models to various deployment formats like ONNX or TensorRT.
- **NVIDIA Jetson Deployment** 🌟 **NEW**: Deploy YOLOv5 on NVIDIA Jetson devices.
- **Test-Time Augmentation (TTA)**: Enhance prediction accuracy with TTA.
- **Model Ensembling**: Combine multiple models for better performance.
- **Model Pruning/Sparsity**: Optimize models for size and speed.
- **Hyperparameter Evolution**: Automatically find the best training hyperparameters.
- **Transfer Learning with Frozen Layers**: Adapt pretrained models to new tasks efficiently using transfer learning.
- **Architecture Summary** 🌟 **NEW**: Understand the YOLOv5 model architecture.
- **Ultralytics HUB Training** 🚀 **RECOMMENDED**: Train and deploy YOLO models using Ultralytics HUB.
- **ClearML Logging**: Integrate with ClearML for experiment tracking.
- **Neural Magic DeepSparse Integration**: Accelerate inference with DeepSparse.
- **Comet Logging** 🌟 **NEW**: Log experiments using Comet ML.  
