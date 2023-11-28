
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
        self.current_x = 0
        self.current_y = 0
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
        self.ser = serial.Serial(self.serial_port, baudrate = self.baudrate, timeout = self.timeout)

    def _setup_plot(self):
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])  # Initialize a line plot
        plt.xlabel('Time')
        plt.ylabel('Voltage')
        plt.title('Real-Time Power Plot')
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%d:%H:%M:%S'))
        plt.xticks(rotation=45, ha='right')  # ha is short for horizontalalignment

    def _setup_plot(self):
        self.fig, self.ax = plt.subplots()
        self.line_voltage, = self.ax.plot([], [], label='Voltage')  # Voltage line
        self.line_power, = self.ax.plot([], [], label='Power', color='red')  # Power line
        plt.xlabel('Time')
        plt.ylabel('Voltage/Power')
        plt.title('Real-Time Power and Voltage Plot')
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
        plt.xticks(rotation=45, ha='right')
        plt.legend()  # Add legend

    def update_data(self, voltage):
        current_time = datetime.now()
        R1 = 5400.0  # R1 in Ohms
        R2 = 1200.0  # R2 in Ohms
        Vin = voltage * (R1 + R2) / R2  # Calculate Vin
        R_panel = 3.0  # Replace with the actual resistance of your solar panel if known

        # Calculate Power (replace this formula if you have the current value)
        power = Vin**2 / R_panel if R_panel else 0  # Power calculation

        # Add new rows to DataFrame
        new_row = {'Timestamp': current_time, 'Panel Voltage': voltage, 'Power': power}
        self.df = self.df.append(new_row, ignore_index=True)

        # Update plot data
        self.line_voltage.set_xdata(self.df['Timestamp'])
        self.line_voltage.set_ydata(self.df['Panel Voltage'])
        self.line_power.set_xdata(self.df['Timestamp'])
        self.line_power.set_ydata(self.df['Power'])
        self.ax.relim()
        self.ax.autoscale_view(True, True, True)
        plt.draw()
        plt.pause(0.001)

    def run(self):
        if(self.ser.in_waiting > 0): #c means confirm receipt, r means ready after startup, d means finished movement. 
            read_byte = self.ser.read(1)
            # Define independent variables
          # print(read_byte)
            if(read_byte == b'r'):
                self.dev_startup = True
                print('hardware is ready')
            elif(read_byte == b'c'):
                print('comfirmed rec by device')
                device_state = 1
            elif(read_byte == b'd'):
                print('device finished movmement')
                device_state = 0
            elif(read_byte == b'p'):
                print('power reporting')
                read_data = self.ser.read(5)
                print(read_data)
                if read_data.endswith(b'q'):
                    # Convert the rest to a number
                    adc_value = int(read_data[:-1])
                    voltage = adc_value*0.02688172043
                    print(f"{voltage}V")
                    self.update_data(voltage)

    def moveToAngle(self,angle_y, angle_x):
        angle_y = int(angle_y*10)
        angle_x = int(-1*angle_x*10)
        self.ser.write(str.encode('a{0},{1}b'.format(angle_y, angle_x)))

    def isDevReady(self):
        return self.isDevReady

        

