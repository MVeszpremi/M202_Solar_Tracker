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



# Set the directory paths
src_dir = './images'
dst_dir = './cloud_position_labeled'

latitude = 34.0522   
longitude = -118.2437

show_debug = 2 #debug level 0, 1 is psoition log, 2 is blocking image display

# A threshold can be adjusted based on the accuracy needed.
threshold = 50

def is_camera_in_shade(polygon, latitude, longitude, image, camera_fov = 120):
    # Calculate the solar position
    site = Location(latitude, longitude, 'America/Los_Angeles', 93, 'Los Angeles')
    site_tz = pytz.timezone('America/Los_Angeles')
    end_time = pd.Timestamp.now(tz=site_tz)
    start_time = end_time - pd.Timedelta(days=1)
   # times = pd.date_range(start=start_time, end=end_time, freq='H', tz=site_tz)

    solpos = solarposition.get_solarposition(end_time, site.latitude, site.longitude, site.altitude)
    
    print(solpos.head())
    
    solar_zenith = solpos['zenith'].iloc[0]
    solar_azimuth = solpos['azimuth'].iloc[0]
    

    height, width, _ = image.shape
    center_x, center_y = width // 2, height // 2

    # Convert azimuth to radians
    azimuth_rad = math.radians(solar_azimuth)

    # Calculate the radius from the center based on solar zenith
    if(solar_zenith <= camera_fov / 2):
        radius = (solar_zenith / camera_fov) * (min(width, height) / 2)
    else:
        radius = 1000

    # Use polar coordinates to get x and y displacement
    displacement_x = abs(radius * math.sin(azimuth_rad))
    displacement_y = abs(radius * math.cos(azimuth_rad))

    # Translate to image coordinates
    sun_x = center_x + int(displacement_x)
    sun_y = center_y - int(displacement_y)

    # Check if sun's position is within a threshold of the cloud's position
    distance = is_point_inside_polygon(sun_x, sun_y, polygon)

    # Draw the sun's position on the image
    cv2.circle(image, (sun_x, sun_y), 10, (0, 255, 255), -1)  # Red circle for sun
    
    if(show_debug >= 1):
         print(f"isSunBlocked: {(distance > -1*threshold)} distance: {distance}, sun_x: {displacement_x}, sun_y: {displacement_y}, sun_rad:{radius}, sun_zenith: {solar_zenith}, sun_azimuth: {solar_azimuth}")

    if(show_debug >= 2):

        # Show the image
        cv2.imshow('Sun and Cloud Position', image)
        cv2.waitKey(0)  # Waits indefinitely until a key is pressed
        cv2.destroyAllWindows()

    return image, (distance > -1*threshold)


# Create the destination directory if it doesn't exist
if not os.path.exists(dst_dir):
    os.makedirs(dst_dir)

def detect_cloud_average_position(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    y, x = np.where(thresh == 255)
    if len(x) == 0 or len(y) == 0:
        return None
    return int(np.mean(x)), int(np.mean(y))

def create_cloud_mask(image):
    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply binary threshold
    _, mask = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
    
    # Refine the mask using morphological operations
    kernel = np.ones((5, 5), np.uint8)  # 5x5 kernel for morphological operations
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    if(show_debug >= 2):

        # Show the image
        cv2.imshow('Mask', mask)
        cv2.waitKey(0)  # Waits indefinitely until a key is pressed
        cv2.destroyAllWindows()
    
    return mask

def draw_hexagon_around_biggest_cloud(image, mask):
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If no contours are found, return the original image
    if not contours:
        return image

    # Sort contours by area and get the biggest one
    biggest_cloud = max(contours, key=cv2.contourArea)

    epsilon = 0.01 * cv2.arcLength(biggest_cloud, True)
    polygon = cv2.approxPolyDP(biggest_cloud, epsilon, True)

    while len(polygon) > 100 and epsilon > 0:
        epsilon += 0.01 * cv2.arcLength(biggest_cloud, True)
        polygon = cv2.approxPolyDP(biggest_cloud, epsilon, True)

    # Draw the hexagon on the image
    cv2.drawContours(image, [polygon], -1, (0, 255, 0), 2)

    return image, polygon

def is_point_inside_polygon(x, y, polygon):
    # Convert polygon to the format suitable for pointPolygonTest
    polygon_np = np.array(polygon).reshape((-1, 1, 2)).astype(np.int32)
    
    # Use the pointPolygonTest function
    distance = cv2.pointPolygonTest(polygon_np, (x, y), True)

    # If the distance is greater than or equal to 0, the point is inside or on the polygon
    return distance



def detect_blue_region_center(image):
    # Threshold to find blue regions
    lower_blue = np.array([90,50,50])
    upper_blue = np.array([140,255,255])
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    y, x = np.where(mask == 255)
    if len(x) == 0 or len(y) == 0:
        return None
    return int(np.mean(x)), int(np.mean(y))

def detect_brightest_spot_avg(image, kernel_size=5):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Create an averaging kernel
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size * kernel_size)
    
    # Convolve the grayscale image with the kernel
    avg_img = cv2.filter2D(gray, -1, kernel)
    
    # Find the maximum location in the convolved image
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(avg_img)
    
    return maxLoc


def draw_cross(image, position, color, size=10):
    cv2.line(image, (position[0] - size, position[1]), (position[0] + size, position[1]), color, 2)
    cv2.line(image, (position[0], position[1] - size), (position[0], position[1] + size), color, 2)

for i in range(1, 100):
    img_path = os.path.join(src_dir, f'{i:04}.png')
    img = cv2.imread(img_path)
    if img is not None:

        # Detect cloud average position
        position = detect_cloud_average_position(img)
        if position is not None:
            draw_cross(img, position, (0, 0, 255))
        else:
            continue

        # Detect center of blue area
        blue_position = detect_blue_region_center(img)
        if blue_position is not None:
            draw_cross(img, blue_position, (255, 0, 0))

        # Detect the brightest spot
        bright_position = detect_brightest_spot_avg(img)
        if bright_position is not None:
            draw_cross(img, bright_position, (0, 0, 0))

        img, polygon = draw_hexagon_around_biggest_cloud(img, create_cloud_mask(img))
        img, shade_status = is_camera_in_shade(polygon, latitude, longitude, img)

            # Convert boolean to string
        text = "True" if shade_status else "False"
        
        # Set the font, size, color, and thickness
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (255, 255, 255) # White color
        thickness = 2
        
        # Get the size of the text
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        
        # Determine the position for the text (top-right corner)
        position = (img.shape[1] - text_size[0] - 10, text_size[1] + 10)
        
        # Put the text on the image
        cv2.putText(img, text, position, font, font_scale, color, thickness)
        print(f"processing: {i}")

        # Save the image to the destination directory
        save_path = os.path.join(dst_dir, f'{i:04}.png')
        cv2.imwrite(save_path, img)

print("Processing complete.")
