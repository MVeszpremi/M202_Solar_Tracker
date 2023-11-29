import cv2
import numpy as np

#Attempt at calibrating the camera and mapping the angles to pixels

# Define the number of corners in the checkerboard pattern
pattern_size = (9, 6)  # Change this according to your checkerboard

# Create arrays to store object points and image points from calibration images
obj_points = []  # 3D points in real-world space
img_points = []  # 2D points in image plane

# Generate a grid of coordinates for the corners in the checkerboard pattern
objp = np.zeros((np.prod(pattern_size), 3), dtype=np.float32)
objp[:, :2] = np.mgrid[0:pattern_size[0], 0:pattern_size[1]].T.reshape(-1, 2)

# Capture calibration images (you'll need several images with the checkerboard pattern at different angles)
# Add the calibration images and their corresponding object points and image points
# Repeat the following block for each calibration image
# ...

# Calibrate the camera
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

# Example FOV and image resolution values (replace these with your actual values)
fov_horizontal_deg = 60  # Horizontal FOV in degrees
fov_vertical_deg = 40    # Vertical FOV in degrees
image_width_pixels = 1920  # Image width in pixels
image_height_pixels = 1080  # Image height in pixels

# Example azimuth and zenith angles (replace these with your calculated angles)
azimuth_deg = 30  # Azimuth angle in degrees
zenith_deg = 20   # Zenith angle in degrees

# Convert angles to pixel ratios
azimuth_rad = np.radians(azimuth_deg)
zenith_rad = np.radians(zenith_deg)

# Convert angles to unit vectors in camera coordinates
direction_vector = np.array([
    np.sin(azimuth_rad) * np.cos(zenith_rad),
    np.sin(zenith_rad),
    np.cos(azimuth_rad) * np.cos(zenith_rad)
])

# Convert unit vector to pixel coordinates
pixel_coords, _ = cv2.projectPoints(direction_vector.reshape(1, 1, 3), np.zeros(3), np.zeros(3), mtx, dist)

azimuth_pixel_ratio = (pixel_coords[0][0][0] / image_width_pixels) * 100  # Convert to percentage
zenith_pixel_ratio = (pixel_coords[0][0][1] / image_height_pixels) * 100  # Convert to percentage

print("Azimuth pixel ratio:", azimuth_pixel_ratio)
print("Zenith pixel ratio:", zenith_pixel_ratio)
