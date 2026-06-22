# Manufacturing_PPE_detection_using_YOLO_and_ESP-32-CAM
A PPE detection computer vision project trained using YOLO V8 model and dataset of about 12k images from roboflow ,model can run locally and analyse PPE detection directly from a ESP 32 live feed


🔥 PPE Detection using ESP32-CAM + YOLO
📌 Project Overview

This project implements a real-time PPE detection system using ESP32-CAM and YOLO object detection. The system is designed to explore AI-based safety monitoring in industrial environments.

🎯 Motivation

The project was inspired by real-world industrial safety challenges where PPE compliance plays a critical role in preventing workplace accidents.

🧠 Tech Stack
>Python
>Ultralytics YOLO V8
>OpenCV
>Arduino (ESP32-CAM)
>Roboflow Dataset
⚙️ System Architecture

ESP32-CAM → WiFi Stream → Python OpenCV → YOLO Model → Detection Output

📷 Features
>Real-time video streaming
>PPE detection (helmet, goggles, etc.)
>Edge device integration (ESP32-CAM)
Live inference using YOLO
⚠️ Limitations
>Model requires further training for better accuracy
>Dataset imbalance affects performance
>Currently experimental prototype
