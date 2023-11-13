import serial
import serial.tools.list_ports
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.animation as animation
from datetime import datetime
import random
import time

arduino_ports = [
    p.device
    for p in serial.tools.list_ports.comports()
    if (('usbmodem' in p.device or 'USB Serial' in p.description))  # may need tweaking to match new arduinos
    ]

for p in serial.tools.list_ports.comports():
    print(p.device)

if not arduino_ports:
    print("[arduino ] Not found")
    exit(0)
if len(arduino_ports) != 1:
    print('[arduino ] More than 1 arduino found')
    exit(0)
print(arduino_ports[0])
time.sleep(2)
ser_1 = serial.Serial(arduino_ports[0], baudrate = 115200, timeout = 0.1)



# Initialize DataFrame
df = pd.DataFrame(columns=['Timestamp', 'Panel Voltage'])
plt.ion()  # Enable interactive mode
fig, ax = plt.subplots()
line, = ax.plot([], [])  # Initialize a line plot
plt.xlabel('Time')
plt.ylabel('Voltage')
plt.title('Real-Time Voltage Plot')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d:%H:%M:%S'))
plt.xticks(rotation=45, ha='right')  # ha is short for horizontalalignment


def update_data(data_point):
    global df, line, ax
    current_time = datetime.now()
    new_row = pd.DataFrame({'Timestamp': [current_time], 'Panel Voltage': [data_point]})
    df = pd.concat([df, new_row], ignore_index=True)
    line.set_xdata(df['Timestamp'])
    line.set_ydata(df['Panel Voltage'])
    ax.relim()
    ax.autoscale_view(True, True, True)
    plt.draw()
    plt.pause(0.01)

desired_rotation_top = 100 #10 degrees
desired_rotation_bottom = 100 #10 degrees


device_state = 0 #0 ready # 1 moving #3 error moving
while(1):
    plt.show(block=False)
    if(ser_1.in_waiting > 0): #c means confirm receipt, r means ready after startup, d means finished movement. 
        read_byte = ser_1.read(1)
        # Define independent variables
        print(read_byte)
        if(read_byte == b'r'):
            ser_1.write(str.encode('a{0},{1}b'.format(desired_rotation_top, desired_rotation_bottom)))
            print('sent test movmement')
        elif(read_byte == b'c'):
            print('comfirmed rec by device')
            device_state = 1
        elif(read_byte == b'd'):
            print('device finished movmement')
            device_state = 0
        elif(read_byte == b'p'):
            print('power reporting')
            read_data = ser_1.read(5)
            print(read_data)
            if read_data.endswith(b'q'):
                # Convert the rest to a number
                adc_value = int(read_data[:-1])
                voltage = adc_value*0.02688172043
                print(f"{voltage}V")
                update_data(voltage)
                


