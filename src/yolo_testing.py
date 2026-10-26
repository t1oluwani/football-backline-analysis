"""Test YOLO11 detection and other functionalities pre-integration."""

from ultralytics import YOLO

# model = YOLO("yolov8n.pt")
# model = YOLO('yolov8m')  
model = YOLO('yolov8x')  

results = model.predict(source="../data/input/Liverpool 3-2 PSG _ VIP Tactical Camera _ 2018 __2235_2245.mp4", save=True)

print(results[0].boxes)
for box in results[0].boxes:
    print(box)   # Print the class label of the detected object