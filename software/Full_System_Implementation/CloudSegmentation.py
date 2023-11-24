import os
import numpy as np
import cv2
import numpy as np
from pvlib import solarposition, tracking
import datetime
import math
import pandas as pd
from shapely.geometry import Point, Polygon
from pvlib.location import Location
import pytz


class CloudSegmentation ():
    def __init__(self, degree_matrix_path = './degree_position_matrix.npy'):
        # Initialize the webcam feed
        self.cap = cv2.VideoCapture(0)  # '0' is usually the default value for the primary camera
        self.degree_matrix = np.load(degree_matrix_path)
        self.ang_x = 0
        self.ang_y = 0
        print("loaded camera angle matrix")
        # Check if the camera opened successfully
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")

        self.sky_image = None

    def capture_image(self):
        # Capture an image from the webcam
        ret, frame = self.cap.read()

        if ret:
            self.sky_image = frame  # Store the captured image in the variable
        else:
            print("Failed to capture image")

    def processForClouds(self):
        if self.sky_image is not None:
            mask = self.create_cloud_mask(self.sky_image)
            if mask is not None:
                img = self.draw_hexagon_around_clouds(self.sky_image, mask)
                
                # Show the image if img is not None
                if img is not None:
                    cv2.imshow('Mask', img)
                    cv2.waitKey(0)  # Waits indefinitely until a key is pressed
                    cv2.destroyAllWindows()
                else:
                    print("Failed to draw hexagon around clouds.")
            else:
                print("Failed to create cloud mask.")
        else:
            print("No image available.")

            


    def create_cloud_mask(self, image):
        # Convert image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Apply binary threshold
        _, mask = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        
        # Refine the mask using morphological operations
        kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel for morphological operations
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        
        return mask

    def draw_hexagon_around_clouds(self, image, mask):
        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # If no contours are found, return the original image
        if not contours:
            return image

        # Sort contours by area in descending order and get the three biggest ones
        sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)[:3]

        for cloud in sorted_contours:
            epsilon = 0.01 * cv2.arcLength(cloud, True)
            polygon = cv2.approxPolyDP(cloud, epsilon, True)

            while len(polygon) > 100 and epsilon > 0:
                epsilon += 0.01 * cv2.arcLength(cloud, True)
                polygon = cv2.approxPolyDP(cloud, epsilon, True)

            # Draw the hexagon on the image
            cv2.drawContours(image, [polygon], -1, (0, 255, 0), 2)

        return image


    def release(self):
        # Release the webcam resource when done
        self.cap.release()
        cv2.destroyAllWindows()

    def setAngle(self,ang_x, ang_y):
        self.ang_x = ang_x
        self.ang_y = ang_y