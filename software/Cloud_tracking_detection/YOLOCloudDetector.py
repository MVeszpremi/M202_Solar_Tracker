import cv2
from ultralytics import YOLO
from picamera2 import Picamera2
import numpy as np

class YOLOCloudDetector:
    def __init__(self, model_path):
        # Initialize the YOLO model
        self.model = YOLO(model_path)

        # Initialize the Raspberry Pi Camera
        self.piCam = Picamera2()
        self.piCam.preview_configuration.main.size = (1280, 720)
        self.piCam.preview_configuration.main.format = "RGB888"
        self.piCam.preview_configuration.align()
        self.piCam.resolution = (1280, 720)
        self.piCam.configure("preview")
        self.piCam.start()

    def detect_clouds(self):
        # Capture a frame
        frame = self.piCam.capture_array()

        # Perform object detection using the YOLO model
        results = self.model(frame)

        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Initialize cloud area count
        cloud_area = 0
        cloud_confidence_threshold = 0.6  # Confidence threshold for cloud detection

        # Iterate over detected objects
        for r in results:
            for box in r.boxes:
                if self.model.names[int(box.cls)] == 'cloud' and box.conf > cloud_confidence_threshold:
                    # Extract bounding box coordinates
                    x1, y1, x2, y2 = box.xyxy
                    # Print bounding box coordinates
                    print(f"Cloud Bounding Box: ({x1:.2f}, {y1:.2f}), ({x2:.2f}, {y2:.2f})")

                    # Calculate the area of the box
                    cloud_area += (x2 - x1) * (y2 - y1)

        # Display the image with annotations
        cv2.imshow("YOLOv8 Detection with Cloud Annotations", annotated_frame)

        # Calculate and print cloud area ratio
        total_area = frame.shape[0] * frame.shape[1]
        cloud_area_ratio = cloud_area / total_area
        print(f"Cloud area: {cloud_area}, Total area: {total_area}, Cloud area ratio: {cloud_area_ratio}")

        # Check for exit condition
        if cv2.waitKey(1) & 0xFF == ord("q"):
            return

# Usage
model_path = '/home/pi/Desktop/cloud/best.pt'
detector = YOLOCloudDetector(model_path)

while True:
    detector.detect_clouds()
