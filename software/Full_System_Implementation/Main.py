from SunPositionDrawer import SunPositionDrawer
from ArduinoSerialInterface import ArduinoSerialInterface, ArduinoSerialInterfaceTesting
from CloudSegmentation import CloudSegmentation
from WeatherChecker import WeatherChecker
from WeatherPredictor import predict_weather
import time
import joblib
import matplotlib.pyplot as plt
import cv2

doNotRotate = False

class Main:
    def __init__(self, location_city, api_weather, svm_classifier):
        plt.ion()  # Enable interactive mode
        self.sun_drawer = SunPositionDrawer()
        self.arduino_interface = ArduinoSerialInterface() #ArduinoSerialInterfaceTesting() 
        self.cloud_segmentation = CloudSegmentation()
        self.weather_checker = WeatherChecker(api_weather, location_city)
        self.svm_classifier = joblib.load(svm_classifier_path)

    def periodic_task_10_second(self):
        print("10s timer")
        cv2.destroyAllWindows()

        # Check the weather using the API
        weather_data = self.weather_checker.get_weather()  # Corrected method name
        api_bad_weather = self.weather_checker.is_bad_weather(weather_data)

        # Use CloudSegmentation to capture and process clouds
        self.cloud_segmentation.capture_image()
        self.cloud_segmentation.processForClouds()

        # Use the camera for weather prediction
        ret, frame = self.cloud_segmentation.get_captured_image()
        if ret:
            weather = predict_weather(frame, self.svm_classifier)
            print("Predicted weather:", weather)
            camera_sunny_weather = weather == "Sunny"
        else:
            camera_sunny_weather = True  # Default to sunny if camera fails

        # Decide the action based on API and camera weather data
        if api_bad_weather and not camera_sunny_weather:
            self.arduino_interface.moveToAngle(-59.0, 0)
            print("Non-sunny or bad weather detected, adjusting solar panel.")
        else:
            if(doNotRotate == False):
                self.arduino_interface.moveToAngle(self.sun_drawer.getRotX(), self.sun_drawer.getRotY())
                self.cloud_segmentation.setErrAngle(self.sun_drawer.getRotXErr(), self.sun_drawer.getRotYErr())

    def periodic_task_2_second(self):
        print(f"CLAMPED: yaw (x):{self.sun_drawer.getRotX()}, pitch(y):{self.sun_drawer.getRotY()}")
        print(f"ERR    : yaw (x):{self.sun_drawer.getRotXErr()}, pitch(y):{self.sun_drawer.getRotYErr()}")

    def run(self):
        last_called = time.time()
        last_called_2 = time.time()
        print("waiting for hardware startup")
        while True:
            cv2.waitKey(1)  # Waits 1ms
            self.arduino_interface.run()
            if (self.arduino_interface.isDevReady()):
                self.sun_drawer.run()
                if time.time() - last_called_2 > 2:
                    self.periodic_task_2_second()
                    last_called_2 = time.time()
                if time.time() - last_called > 10:
                    self.periodic_task_10_second()  # Call the periodic function
                    last_called = time.time()  # Reset the timer


if __name__ == "__main__":
    svm_classifier_path = './svm_classifier.joblib'  # update the path
    svm_classifier = joblib.load(svm_classifier_path)
    main = Main(location_city='Los Angeles', api_weather='32b8600ccd902c30801c6fe5ac806afa',
                svm_classifier=svm_classifier)
    main.run()
