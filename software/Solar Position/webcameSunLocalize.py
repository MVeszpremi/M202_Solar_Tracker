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

latitude = 34.0522   
longitude = -118.2437

camera_fov = 170


def make_square_with_padding(img):
    height, width = img.shape[:2]

    # Calculate the difference and the padding needed
    if width > height:
        delta = width - height
        top, bottom = delta // 2, delta - (delta // 2)
        left, right = 0, 0
    else:
        delta = height - width
        top, bottom = 0, 0
        left, right = delta // 2, delta - (delta // 2)

    # Create a border around the image to make it square
    color = [0, 0, 0]  # Color of border, black in this example
    new_img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)
    
    return new_img

# Initialize the webcam capture object
cap = cv2.VideoCapture(0)

# Check if the webcam is opened successfully
if not cap.isOpened():
    raise IOError("Cannot open webcam")

# Coordinate for the circle
circle_center = (250, 250)  # Change to your desired coordinates
circle_radius = 30  # Radius of the circle
circle_color = (0, 255, 255)  # Circle color in BGR (blue, green, red)
circle_thickness = 10  # Thickness of the circle outline

site = Location(latitude, longitude, 'America/Los_Angeles', 93, 'Los Angeles')
site_tz = pytz.timezone('America/Los_Angeles')
end_time = pd.Timestamp.now(tz=site_tz)
start_time = end_time - pd.Timedelta(days=1)
# times = pd.date_range(start=start_time, end=end_time, freq='H', tz=site_tz)

solpos = solarposition.get_solarposition(end_time, site.latitude, site.longitude, site.altitude)



print(solpos.head())

solar_zenith = solpos['zenith'].iloc[0]
solar_azimuth = solpos['azimuth'].iloc[0]


try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break
        frame = make_square_with_padding(frame)
        height, width, _ = frame.shape
        center_x, center_y = width // 2, height // 2

        # Convert azimuth to radians
        azimuth_rad = math.radians(solar_azimuth)

        # Calculate the radius from the center based on solar zenith
        if(solar_zenith <= camera_fov / 2):
            radius = (solar_zenith / (camera_fov/2)) * (min(width, height) / 2)
        else:
            radius = 10000

        # Use polar coordinates to get x and y displacement
        displacement_x = abs(radius * math.sin(azimuth_rad))
        displacement_y = abs(radius * math.cos(azimuth_rad))

        # Translate to image coordinates
        sun_x = center_x + int(displacement_x)
        sun_y = center_y + int(displacement_y)

        print(f"sun_x: {displacement_x}, sun_y: {displacement_y}, sun_rad:{radius}, sun_zenith: {solar_zenith}, sun_azimuth: {solar_azimuth}")


        # Draw a circle on the frame
        cv2.circle(frame, (sun_x, sun_y), circle_radius, circle_color, circle_thickness)

        # Display the resulting frame
        cv2.imshow('Webcam View', frame)

        # Press 'q' on the keyboard to exit the loop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()
