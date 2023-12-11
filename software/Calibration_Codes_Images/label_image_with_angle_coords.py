from PIL import Image, ImageDraw, ImageFont
import numpy as np
import cv2


degree_matrix_path = './degree_position_matrix.npy'
degree_matrix = np.load(degree_matrix_path)

# Load the image
image_path = './frame_to_label.png'  # Replace with the path to your image
image = cv2.imread(image_path)

# Define the text, font, location, font size, and color
font = cv2.FONT_HERSHEY_PLAIN
font_color = (0, 0, 255)  # BGR color (e.g., red is (0, 0, 255))

# Calculate the font thickness (optional)
font_thickness = 2

# Calculate the font scale based on font size
font_scale = 1


texts_to_write = []
for x in range (0, 940, 100):
    for y in range(0, 520, 100):
        image = cv2.putText(image, ('('+str(round(degree_matrix[y, x, 0])) + ', '+str(round(degree_matrix[y, x, 1])) +')'), (x, y), font, font_scale, font_color, font_thickness)

# Save or display the image with text
output_image_path = './frame_labelled.png'  # Replace with the desired output path
cv2.imwrite(output_image_path, image)

# Display the image (optional)
cv2.imshow('Image with Text', image)
cv2.waitKey(0)
cv2.destroyAllWindows()