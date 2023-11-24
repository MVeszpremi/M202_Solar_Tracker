
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import pvlib
from datetime import datetime
from pvlib import solarposition, tracking
import math
import pandas as pd
from shapely.geometry import Point, Polygon
from pvlib.location import Location
import pytz

class SunPositionDrawer ():
    def __init__(self, interval = 5, latitude = 34.05, longitude = -118.25):
        # Initialization code, if any, can go here
        super().__init__()
        self.interval = interval
        self.latitude = latitude
        self.longitude = longitude
        self.rot_x = 0
        self.rot_y = 0
        fig = plt.figure()
        self.ax = fig.add_subplot(111, projection='3d')

    def run(self):
        # Get current date and time
        current_time = datetime.now()

        site = Location(self.latitude, self.longitude, 'America/Los_Angeles', 93, 'Los Angeles')
        site_tz = pytz.timezone('America/Los_Angeles')
        end_time = pd.Timestamp.now(tz=site_tz)
        start_time = end_time - pd.Timedelta(hours=9)
    # times = pd.date_range(start=start_time, end=end_time, freq='H', tz=site_tz)

        solpos = solarposition.get_solarposition(end_time, site.latitude, site.longitude, site.altitude)

        
        solar_zenith = solpos['zenith'].iloc[0]
        solar_azimuth = solpos['azimuth'].iloc[0]

        # Convert to 3D coordinates
        x, y, z = self.spherical_to_cartesian(solar_zenith, solar_azimuth)

        # Clear previous data
        self.ax.clear()

        # Redraw the elements

        # Equator line
    # Equator line drawn clockwise
        u_eq = np.linspace(0, 2 * np.pi, 100)  
        self.ax.plot(np.cos(u_eq), np.sin(u_eq), 0, color="b", alpha=0.3)

        # Define compass points (updated for clockwise azimuth)
        compass_points = {'N': 0, 'E': 270, 'S': 180, 'W': 90}

        # Label compass points
        for point, angle in compass_points.items():
            angle_rad = np.radians(angle)
            label_x = np.cos(angle_rad)
            label_y = np.sin(angle_rad)
            self.ax.text(label_x, label_y, 0, point, color="red", fontsize=12, ha='center', va='center')

        # Four dome lines (updated for clockwise azimuth)
        v_dom = np.linspace(0, np.pi, 100)
        for angle in [0, 270, 180, 90]:
            angle_rad = np.radians(angle)
            self.ax.plot(np.cos(angle_rad) * np.sin(v_dom), np.sin(angle_rad) * np.sin(v_dom), np.cos(v_dom), color="b", alpha=0.3)

        # Sun's position
        self.ax.scatter(x, y, z, color='yellow', s=100)

        # Line to sun's position
        self.ax.plot([0, x], [0, y], [0, z], color='red')

        # Rectangle
        rectangle_width = 0.4
        rectangle_height = 0.2
        rectangle_vertices = self.calculate_centered_rectangle_vertices(x, y, z, rectangle_width, rectangle_height)
        rectangle = Poly3DCollection([rectangle_vertices], color='cyan', alpha=0.6)
        self.ax.add_collection3d(rectangle)

        # Axis labels
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.set_zlabel('z')

        # Degree angles for azimuth and elevation
        for angle in range(0, 360, 30):
            self.ax.text(np.cos(np.radians(angle)), np.sin(np.radians(angle)), 0, f"{angle}°", color="green")
        for angle in range(0, 180, 30):
            self.ax.text(0, np.sin(np.radians(angle)), np.cos(np.radians(angle)), f"{angle}°", color="blue")

        # Title
        self.ax.set_title('Live Sun Position on Spherical Coordinates')
        plt.draw()
        plt.pause(0.001)


    def clamp(self, value, min_value, max_value):
    
        return max(min_value, min(value, max_value))

    def spherical_to_cartesian(self, zenith, azimuth):
        r = 1  # unit sphere
        azimuth_rad = np.radians(360 - azimuth)  # Clockwise from North
        zenith_rad = np.radians(zenith)
        x = r * np.sin(zenith_rad) * np.cos(azimuth_rad)
        y = r * np.sin(zenith_rad) * np.sin(azimuth_rad)
        z = r * np.cos(zenith_rad)
        return x, y, z
    
    def calculate_centered_rectangle_vertices(self, sun_x, sun_y, sun_z, width, height):
        sun_direction = np.array([sun_x, sun_y, sun_z])
        sun_direction /= np.linalg.norm(sun_direction)

        # Pitch: Angle between the sun direction projection on YZ plane and Y-axis

        pitch = -np.arctan2(sun_direction[1], sun_direction[2])

        pitch = self.clamp(pitch, (-27.5)*(np.pi/180), 27.5*(np.pi/180))

        # Apply pitch rotation (around X-axis)
        rot_x = np.array([[1, 0, 0],
                        [0, np.cos(pitch), -np.sin(pitch)],
                        [0, np.sin(pitch), np.cos(pitch)]])
        sun_direction_pitch_rotated = np.dot(rot_x, sun_direction)

        # Yaw: Angle between the sun direction projection on XY plane and X-axis
        yaw =np.arctan2(sun_direction_pitch_rotated[0], sun_direction_pitch_rotated[2])
        yaw = self.clamp(yaw, -60.0*(np.pi/180), 27.5*(np.pi/180))
        print(f"yaw (x):{yaw*(180/np.pi)}, pitch(y):{pitch*(180/np.pi)}")
        self.rot_x = yaw*(180/np.pi)
        self.rot_y = pitch*(180/np.pi)
        # Apply yaw rotation (around Y-axis)
        rot_y = np.array([[np.cos(yaw), 0, np.sin(yaw)],
                        [0, 1, 0],
                        [-np.sin(yaw), 0, np.cos(yaw)]])
        sun_direction_yaw_rotated = np.dot(rot_y, sun_direction_pitch_rotated)

        # Define initial rectangle in the XY plane
        half_width = width / 2
        half_height = height / 2
        rectangle = np.array([[half_width, half_height, 0],
                            [-half_width, half_height, 0],
                            [-half_width, -half_height, 0],
                            [half_width, -half_height, 0]])

        # Apply pitch and yaw rotations
        rectangle = np.dot(rectangle, rot_x.T)
        rectangle = np.dot(rectangle, rot_y.T)

        return rectangle
    
    def getRotX(self):
        return self.rot_x

    def getRotY(self):
        return self.rot_y
