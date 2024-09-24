import cv2
import torch

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

def detect_car(frame):
    results = model(frame)
    for detection in results.xyxy[0]:
        label = results.names[int(detection[5])]
        if label == 'car':
            return True
    return False
