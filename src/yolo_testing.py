"""Test YOLO11 detection and other functionalities pre-integration."""

from ultralytics import YOLO

VIDEO_NAME = "Liverpool 3-2 PSG _ VIP Tactical Camera _ 2018 __2235_2245.mp4"
VIDEO_PATH = f"../data/input/{VIDEO_NAME}"

# model = YOLO('models/yolov8m')  
model = YOLO('models/yolov8x')  

results = model.predict(source=VIDEO_PATH, save=True)

print(results[0].boxes)
for box in results[0].boxes:
    print(box) 