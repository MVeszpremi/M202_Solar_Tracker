import cv2
import numpy as np

#Attempt 2 utilizes more calibration and validation techniques
#See description for more detail

# Define the checkerboard pattern size
pattern_size = (9, 6)  # Change this according to your checkerboard

# Arrays to store object points and image points from calibration images
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
fov_horizontal_deg = 180  # Horizontal FOV in degrees for a fisheye lens
fov_vertical_deg = 180    # Vertical FOV in degrees for a fisheye lens
image_width_pixels = 1920  # Image width in pixels
image_height_pixels = 1080  # Image height in pixels

# Validate the mapping accuracy using validation angles and corresponding pixels
# Example validation angles (replace these with your validation data)
validation_azimuth_deg = [30, 45, 60]
validation_zenith_deg = [20, 35, 50]
# Corresponding validation pixel coordinates (based on ground truth or measurements)
validation_pixels = [(100, 200), (300, 400), (500, 600)]

# Perform the mapping for validation angles
for i in range(len(validation_azimuth_deg)):
    azimuth_deg = validation_azimuth_deg[i]
    zenith_deg = validation_zenith_deg[i]

    # Convert angles to radians
    azimuth_rad = np.radians(azimuth_deg)
    zenith_rad = np.radians(zenith_deg)

    # Convert angles to unit vectors in camera coordinates
    direction_vector = np.array([
        np.sin(azimuth_rad) * np.cos(zenith_rad),
        np.sin(zenith_rad),
        np.cos(azimuth_rad) * np.cos(zenith_rad)
    ])

    # Convert unit vector to pixel coordinates using equidistant projection
    focal_length = 1000  # Replace this with the focal length of your fisheye camera (in pixels)

    # Equidistant projection for fisheye lens
    theta = np.arctan2(np.linalg.norm(direction_vector[:2]), direction_vector[2])
    r = 2 * np.tan(theta / 2)

    # Calculate pixel coordinates using radial distance
    azimuth_pixel = (r * np.cos(azimuth_rad) * focal_length) + (image_width_pixels / 2)
    zenith_pixel = (r * np.sin(azimuth_rad) * focal_length) + (image_height_pixels / 2)

    # Compare with validation pixels
    validation_pixel = validation_pixels[i]
    print(f"Validation {i + 1}:")
    print("Expected Pixel Coordinate:", validation_pixel)
    print("Calculated Pixel Coordinate:", (azimuth_pixel, zenith_pixel))
    print("------------")
