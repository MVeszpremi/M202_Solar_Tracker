from SunPositionDrawer import SunPositionDrawer
from ArduinoSerialInterface import ArduinoSerialInterface
from CloudSegmentation import CloudSegmentation
from WeatherChecker import WeatherChecker
from WeatherPredictor import WeatherPredictor
import time
import matplotlib.pyplot as plt
import cv2

class Main:
    def __init__(self, location_city, api_weather, svm_classifier):
        plt.ion()  # Enable interactive mode
        self.sun_drawer = SunPositionDrawer()
        self.arduino_interface = ArduinoSerialInterface()
        self.cloud_segmentation = CloudSegmentation()
        self.weather_checker = WeatherChecker(api_weather, location_city)
        self.weather_predictor = WeatherPredictor(svm_classifier)



    def periodic_task_10_second(self):
        print("10s timer")
        cv2.destroyAllWindows()
        self.cloud_segmentation.capture_image()
        self.cloud_segmentation.processForClouds()
        current_bad_weather = self.weather_checker.check_current_severe_weather()
        ret, frame = self.weather_predictor.cap.read()
        if ret:
            # The camera detects if the current weather is sunny
            current_sunny_weather_cam = self.weather_predictor.predict_weather(frame) == "Sunny"

            # If the API and camera test results do not match, the camera results will prevail
            current_sunny_weather = current_sunny_weather_cam if current_sunny_weather_api != current_sunny_weather_cam else current_sunny_weather_api
        else:
            # If it is not possible to read frames from the camera, use the API result
            current_sunny_weather = current_sunny_weather_api

        if not current_sunny_weather:
            self.arduino_interface.moveToAngle(-59.0, 0)
            print("Non-sunny weather is currently present.")

        else:
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
            if(self.arduino_interface.isDevReady()):
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
    main = Main(location_city='Los Angeles', api_weather = '32b8600ccd902c30801c6fe5ac806afa')
    main.run()
