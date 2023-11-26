from SunPositionDrawer import SunPositionDrawer
from ArduinoSerialInterface import ArduinoSerialInterface
from CloudSegmentation import CloudSegmentation
import time
import matplotlib.pyplot as plt
import cv2

class Main:
    def __init__(self):
        plt.ion()  # Enable interactive mode
        self.sun_drawer = SunPositionDrawer()
        self.arduino_interface = ArduinoSerialInterface()
        self.cloud_segmentation = CloudSegmentation()


    def periodic_task_10_second(self):
        print("10s timer")
        cv2.destroyAllWindows()
        self.cloud_segmentation.capture_image()
        self.cloud_segmentation.processForClouds()
        self.arduino_interface.moveToAngle(self.sun_drawer.getRotX(), self.sun_drawer.getRotY())
        self.cloud_segmentation.setAngle(self.sun_drawer.getRotX(), self.sun_drawer.getRotY())

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
    main = Main()
    main.run()
