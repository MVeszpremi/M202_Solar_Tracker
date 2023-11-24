from SunPositionDrawer import SunPositionDrawer
from ArduinoSerialInterface import ArduinoSerialInterface
from CloudSegmentation import CloudSegmentation
import time
import matplotlib.pyplot as plt

class Main:
    def __init__(self):
        plt.ion()  # Enable interactive mode
        self.sun_drawer = SunPositionDrawer()
        self.arduino_interface = ArduinoSerialInterface()
        self.cloud_segmentation = CloudSegmentation()


    def periodic_task_10_second(self):
        print("10s timer")
        self.cloud_segmentation.capture_image()
        self.cloud_segmentation.processForClouds()


    def run(self):
        last_called = time.time()
        while True:
            self.arduino_interface.run()
            self.sun_drawer.run()
            if time.time() - last_called > 10:
                self.periodic_task_10_second()  # Call the periodic function
                last_called = time.time()  # Reset the timer

if __name__ == "__main__":
    main = Main()
    main.run()
