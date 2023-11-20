import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load the degree matrix
degree_matrix_path = './degree_position_matrix.npy'
degree_matrix = np.load(degree_matrix_path)

print(degree_matrix)

# Assuming we know the image size
image_width = 930  # Replace with the actual image width
image_height = 510  # Replace with the actual image height

# Create a figure and axis for plotting
fig, ax = plt.subplots()

# Set the size of the figure
fig.set_size_inches(image_width / 100, image_height / 100)

# Generate a meshgrid for the X and Y axes
X, Y = np.meshgrid(range(image_width), range(image_height))

# Now, draw the grid lines
# Draw horizontal lines
for i in range(15, image_height, 5):  # Adjust the step size to your preference
    ax.plot(degree_matrix[i, :, 0], degree_matrix[i, :, 1], color='blue', linewidth=0.5)

# Draw vertical lines
for j in range(10, image_width, 5):  # Adjust the step size to your preference
    ax.plot(degree_matrix[:, j, 0], degree_matrix[:, j, 1], color='blue', linewidth=0.5)

# Invert the Y axis since image coordinates are top left, but plot is bottom left
ax.invert_yaxis()

# Hide the axes
ax.axis('off')

plt.show()
