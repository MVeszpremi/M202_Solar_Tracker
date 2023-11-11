import cv2
import requests
from ultralytics import YOLO
from picamera2 import Picamera2
import time

# OpenWeatherMap API setup
API_KEY = '32b8600ccd902c30801c6fe5ac806afa'
CITY_NAME = 'Los Angeles'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

# YOLO setup
model_path = '/home/pi/Desktop/cloud/best.pt'  # Make sure this is the correct path
model = YOLO(model_path)

# Raspberry Pi Camera setup
piCam = Picamera2()
piCam.preview_configuration.main.size = (1280,720)
piCam.preview_configuration.main.format = "RGB888"
piCam.preview_configuration.align()
piCam.resolution = (1280, 720)
piCam.configure("preview")
piCam.start()

# Function to get the weather
def get_weather(api_key, city_name):
    url = BASE_URL + "appid=" + api_key + "&q=" + city_name
    response = requests.get(url)
    return response.json()

# Function to check for bad weather
def is_bad_weather(weather_data):
    bad_weather_conditions = ['Rain', 'Snow', 'Hail', 'Sleet', 'Freeze', 'Cold', 'Wind', 'Heat', 'Heavy Rain', 'Continuous Rain']
    if 'weather' in weather_data:
        for weather in weather_data['weather']:
            if weather['main'] in bad_weather_conditions:
                return True
    return False

# Function to check if the weather is clear or cloudy
def is_clear_or_cloudy(weather_data):
    if 'weather' in weather_data:
        for weather in weather_data['weather']:
            if weather['main'] in ['Clear', 'Clouds']:
                return True
    return False

# Set the check interval to half an hour
check_interval = 1800  # Seconds
last_check = time.time()

# Get initial weather data
weather_data = get_weather(API_KEY, CITY_NAME)

# Main loop
while True:
    current_time = time.time()
    if current_time - last_check > check_interval:
        weather_data = get_weather(API_KEY, CITY_NAME)
        last_check = current_time

    # If the weather is bad, do not perform detection and stop the camera
    if is_bad_weather(weather_data):
        piCam.stop()  # Stop the camera
        time.sleep(check_interval)  # Wait for the next check cycle
        continue  # Continue to the next iteration of the loop
    else:
        if not piCam.started:
            piCam.start()  # Restart the camera

        frame = piCam.capture_array()

        # If the weather is clear or cloudy, perform detection
        if is_clear_or_cloudy(weather_data):
            results = model(frame)
            annotated_frame = results[0].plot()

            # Convert to grayscale
            gray = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2GRAY)
            ret, binary = cv2.threshold(gray, 175, 255, cv2.THRESH_BINARY)

            # Find contours
            contours, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            cv2.drawContours(annotated_frame, contours, -1, (0, 0, 255), 3)

            # Show the image with contours
            cv2.imshow("YOLOv8 Inference with Contours", annotated_frame)

        # Condition to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Cleanup resources
cv2.destroyAllWindows()
piCam.stop()
