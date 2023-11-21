import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

class DataPlotter:
    def __init__(self):
        self.df = pd.DataFrame(columns=['Timestamp', 'Panel Voltage'])
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [])
        plt.xlabel('Time')
        plt.ylabel('Voltage')
        plt.title('Real-Time Voltage Plot')
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%d:%H:%M:%S'))
        plt.xticks(rotation=45, ha='right')

    def update_data(self, data_point):
        current_time = datetime.now()
        new_row = pd.DataFrame({'Timestamp': [current_time], 'Panel Voltage': [data_point]})
        self.df = pd.concat([self.df, new_row], ignore_index=True)
        self.line.set_xdata(self.df['Timestamp'])
        self.line.set_ydata(self.df['Panel Voltage'])
        self.ax.relim()
        self.ax.autoscale_view(True, True, True)
        plt.draw()
        plt.pause(0.01)
