import cv2
import numpy as np

# Global list to store points
points = []

def click_event(event, x, y, flags, params):
    # If left mouse button clicked, save the coordinate of the click
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

        # Display the point on the image
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)
        cv2.imshow('Image', img)

# Load the image
image_path = './frame-0.0.png'
img = cv2.imread(image_path)
cv2.imshow('Image', img)

# Set the mouse callback function to 'click_event'
cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the points to a file
np.save('./manual_points.npy', np.array(points))

# Print out the list of points
print("Collected points:")
print(points)
