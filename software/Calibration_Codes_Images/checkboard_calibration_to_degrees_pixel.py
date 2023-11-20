import cv2
import numpy as np

# Load the saved calibration points (2D image points)
calibration_data_path = 'manual_points.npy'  # Update this path
image_points_loaded = np.load(calibration_data_path)

# Chessboard parameters
chessboard_size = (9, 5)  # Update with the actual size of your chessboard (internal corners)
square_size = 28  # in mm

# Assuming the image size is known
image_width = 960  # Replace with the actual image width
image_height = 540  # Replace with the actual image height

# Generate corresponding 3D object points
object_points = np.zeros((np.prod(chessboard_size), 3), np.float32)
object_points[:, :2] = np.indices(chessboard_size).T.reshape(-1, 2)
object_points *= square_size

# Replicate object points for each calibration image
# Assuming all points are from a single image, if multiple images, replicate accordingly
object_points = [object_points] #* len(image_points_loaded)

#print(object_points)
image_points = np.array([image_points_loaded.reshape(-1, 1, 2)], dtype=np.float32)
#print(image_points)
# Camera calibration
ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(
    object_points, image_points, (image_width, image_height), None, None)



# Initialize an array for the angles
angle_matrix = np.zeros((image_height, image_width, 2), dtype=np.float32)

# Calculate the angles for each coordinate considering the distortion
for i in range(image_height):
    for j in range(image_width):
        # Undistort the points
        undistorted_point = cv2.undistortPoints(
            np.array([[[j, i]]], dtype=np.float32), camera_matrix, dist_coeffs, None, camera_matrix)

        # Calculate the angles
        x, y = undistorted_point[0, 0, 0], undistorted_point[0, 0, 1]
        angle_x = np.arctan2(x - camera_matrix[0, 2], camera_matrix[0, 0])
        angle_y = np.arctan2(y - camera_matrix[1, 2], camera_matrix[1, 1])
        
        angle_matrix[i, j] = [np.degrees(angle_x), np.degrees(angle_y)]

# Save the angle matrix
angle_matrix_path = 'degree_position_matrix.npy'  # Update this path
np.save(angle_matrix_path, angle_matrix)

print(f"Angle matrix saved at {angle_matrix_path}")

