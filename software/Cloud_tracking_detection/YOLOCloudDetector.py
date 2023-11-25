import cv2
from ultralytics import YOLO
from picamera2 import Picamera2

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

    def detect_objects_and_clouds(self):
        # Capture a frame
        frame = self.piCam.capture_array()

        # Perform object detection using the YOLO model
        results = self.model(frame)
        annotated_frame = results[0].plot()

        # Convert to grayscale for cloud detection
        gray = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)

        # Find contours of clouds
        contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(annotated_frame, contours, -1, (0, 0, 255), 3)

        # Display the image with cloud contours
        cv2.imshow("YOLOv8 Detection with Cloud Contours", annotated_frame)

        # Check for exit condition
        if cv2.waitKey(1) & 0xFF == ord("q"):
            return

# Usage
model_path = '/home/pi/Desktop/cloud/best.pt'  # Ensure this is the correct model path
detector = YOLOCloudDetector(model_path)

# Continuously detect objects and clouds
while True:
    detector.detect_objects_and_clouds()
