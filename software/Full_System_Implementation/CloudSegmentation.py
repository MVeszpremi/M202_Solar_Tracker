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
        print("processing for clouds")

    def release(self):
        # Release the webcam resource when done
        self.cap.release()
        cv2.destroyAllWindows()