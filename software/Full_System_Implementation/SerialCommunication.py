import threading
import serial
import serial.tools.list_ports
import time

class SerialCommunication(threading.Thread):
    def __init__(self, desired_rotation_y, desired_rotation_x):
        threading.Thread.__init__(self)
        self.desired_rotation_y = desired_rotation_y
        self.desired_rotation_x = desired_rotation_x
        self.ser_1 = self.initialize_serial()

    def run(self):
        while True:
            self.read_write_serial()
            time.sleep(0.1)  # Adjust as needed

    def initialize_serial(self):
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
        self.ser_1 = serial.Serial(arduino_ports[0], baudrate = 115200, timeout = 0.1)


    def read_write_serial(self):
       if(self.ser_1.in_waiting > 0): #c means confirm receipt, r means ready after startup, d means finished movement. 
            read_byte = self.ser_1.read(1)
            # Define independent variables
            print(read_byte)
            if(read_byte == b'r'):
                self.ser_1.write(str.encode('a{0},{1}b'.format(self.desired_rotation_y, self.desired_rotation_x)))
                print('sent test movmement')
            elif(read_byte == b'c'):
                print('comfirmed rec by device')
                device_state = 1
            elif(read_byte == b'd'):
                print('device finished movmement')
                device_state = 0
            elif(read_byte == b'p'):
                print('power reporting')
                read_data = self.ser_1.read(5)
                print(read_data)
                if read_data.endswith(b'q'):
                    # Convert the rest to a number
                    adc_value = int(read_data[:-1])
                    voltage = adc_value*0.02688172043
                    print(f"{voltage}V")
                    return voltage
