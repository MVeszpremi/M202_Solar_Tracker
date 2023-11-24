from SunPositionDrawer import SunPositionDrawer
from ArduinoSerialInterface import ArduinoSerialInterface
import time

class Main:
    def __init__(self):
        self.sun_drawer = SunPositionDrawer()
        self.arduino_interface = ArduinoSerialInterface()


    def periodic_task_5_second(self):
        self.sun_drawer.run()

    def run(self):
        last_called = time.time()-5
        while True:
            self.arduino_interface.run()
            if time.time() - last_called > 5:
                self.periodic_task_5_second()  # Call the periodic function
                last_called = time.time()  # Reset the timer

if __name__ == "__main__":
    main = Main()
    main.run()
