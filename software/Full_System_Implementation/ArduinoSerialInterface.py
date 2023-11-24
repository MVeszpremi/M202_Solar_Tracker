
import serial
import serial.tools.list_ports
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.animation as animation
from datetime import datetime
import random
import time

class ArduinoSerialInterface:
    def __init__(self, baudrate=115200, timeout=0.1):
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial_port = None
        self.dev_startup = False
        self.df = pd.DataFrame(columns=['Timestamp', 'Panel Voltage'])
        self._setup_plot()
        self._find_arduino()

    def _find_arduino(self):
        arduino_ports = [
            p.device
            for p in serial.tools.list_ports.comports()
            if (('usbmodem' in p.device or 'USB Serial' in p.description))  
        ]
        if not arduino_ports:
            print("[arduino ] Not found")
            exit(0)
        if len(arduino_ports) != 1:
            print('[arduino ] More than 1 arduino found')
            exit(0)
        self.serial_port = arduino_ports[0]
        print(self.serial_port)
        time.sleep(2)
        self.ser = serial.Serial(self.serial_port, baudrate = self.baudrate, timeout = self.timeout)

    def _setup_plot(self):
        plt.ion()  # Enable interactive mode
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])  # Initialize a line plot
        plt.xlabel('Time')
        plt.ylabel('Voltage')



    def update_data(self,data_point):
        current_time = datetime.now()
        new_row = pd.DataFrame({'Timestamp': [current_time], 'Panel Voltage': [data_point]})
        df = pd.concat([df, new_row], ignore_index=True)
        self.line.set_xdata(df['Timestamp'])
        self.line.set_ydata(df['Panel Voltage'])
        self.ax.relim()
        self.ax.autoscale_view(True, True, True)
        plt.draw()
        plt.pause(0.01)

    def run(self):
        if(self.serial_port.in_waiting > 0): #c means confirm receipt, r means ready after startup, d means finished movement. 
            read_byte = self.serial_port.read(1)
            # Define independent variables
            print(read_byte)
            if(read_byte == b'r'):
                self.dev_startup = True
                print('sent test movmement')
            elif(read_byte == b'c'):
                print('comfirmed rec by device')
                device_state = 1
            elif(read_byte == b'd'):
                print('device finished movmement')
                device_state = 0
            elif(read_byte == b'p'):
                print('power reporting')
                read_data = self.serial_port.read(5)
                print(read_data)
                if read_data.endswith(b'q'):
                    # Convert the rest to a number
                    adc_value = int(read_data[:-1])
                    voltage = adc_value*0.02688172043
                    print(f"{voltage}V")
                    self.update_data(voltage)

    def moveToAngle(self,angle_y, angle_x):
        self.serial_port.write(str.encode('a{0},{1}b'.format(angle_y, angle_x)))

        

