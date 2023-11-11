import serial
import serial.tools.list_ports
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


desired_rotation_top = 100 #10 degrees
desired_rotation_bottom = 100 #10 degrees
while(1):
    if(ser_1.in_waiting > 0):
        read_byte = ser_1.read(1)
        # Define independent variables
        print(read_byte)
        if(read_byte == b'r'):
            ser_1.write(str.encode('a{0},{1}b'.format(desired_rotation_top, desired_rotation_bottom)))
            print('sent test movmement')