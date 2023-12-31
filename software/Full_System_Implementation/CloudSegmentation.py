import os
import numpy as np
import cv2
import numpy as np
from pvlib import solarposition, tracking
from datetime import datetime
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
        self.ang_x_err = 0
        self.ang_y_err = 0
        print("loaded camera angle matrix")
        # Check if the camera opened successfully
        if not self.cap.isOpened():
            raise IOError("Cannot open webcam")

        self.sky_image = None

    def capture_image(self):
        # Capture an image from the webcam
        ret, frame = self.cap.read()

        if ret:
            # Scale down the image by a factor of two
            scaled_frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))
            self.sky_image = scaled_frame  # Store the scaled image in the variable
        else:
            print("Failed to capture image")
            
    def get_captured_image(self):
        """Returns the most recently captured image and its status"""
        if self.capture_image():
            return True, self.sky_image
        else:
            return False, None
    def processForClouds(self):
        if self.sky_image is not None:
            mask = self.create_cloud_mask(self.sky_image)
            if mask is not None:
                img = self.draw_hexagon_around_clouds(self.sky_image, mask)
                
                y, x = self.find_closest(-1*self.ang_x_err, -1*self.ang_y_err)

                color = (0, 255, 255)  # Yellow in BGR format
                radius = 5  # Radius of 5 to create a dot of size 10

                # Draw the circle
                cv2.circle(img, (x,y), radius, color, -1)
                # Show the image if img is not None
                if img is not None:
                    cv2.imshow('Mask', img)
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"{timestamp}.png"

                    # Save the image
                    file_path = os.path.join("../../data/captured_sky", filename)
                    cv2.imwrite(file_path, img)
                else:
                    print("Failed to draw hexagon around clouds.")
            else:
                print("Failed to create cloud mask.")
        else:
            print("No image available.")

            
    def find_closest(self, find_closest_x, find_closest_y):
        min_distance = float('inf')
        closest_i, closest_j = -1, -1

        for i in range(self.degree_matrix.shape[0]):
            for j in range(self.degree_matrix.shape[1]):
                x, y = self.degree_matrix[i, j]
                distance = np.sqrt((x - find_closest_x) ** 2 + (y - find_closest_y) ** 2)
                if distance < min_distance:
                    min_distance = distance
                    closest_i, closest_j = i, j

        return closest_i, closest_j


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

            M = cv2.moments(cloud)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                font = cv2.FONT_HERSHEY_PLAIN
                font_color = (0, 0, 255)  # BGR color (e.g., red is (0, 0, 255))
                # Calculate the font thickness (optional)
                font_thickness = 1
                # Calculate the font scale based on font size
                font_scale = 2
                image = cv2.putText(image, ('('+str(round(self.degree_matrix[cY, cX, 0])) + ', '+str(round(self.degree_matrix[cY, cX, 1])) +')'), (cX, cY), font, font_scale, font_color, font_thickness)
            
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

    def setErrAngle(self,ang_x, ang_y):
        self.ang_x_err = ang_x
        self.ang_y_err = ang_y
