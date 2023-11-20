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


def spherical_to_cartesian(zenith, azimuth):
    r = 1  # unit sphere
    azimuth_rad = np.radians(360 - azimuth)  # Clockwise from North
    zenith_rad = np.radians(zenith)
    x = r * np.sin(zenith_rad) * np.cos(azimuth_rad)
    y = r * np.sin(zenith_rad) * np.sin(azimuth_rad)
    z = r * np.cos(zenith_rad)
    return x, y, z


# # Function to calculate rectangle vertices
# def calculate_centered_rectangle_vertices(x, y, z, width, height):
#     sun_direction = np.array([x, y, z])
#     sun_direction /= np.linalg.norm(sun_direction)
#     if sun_direction[2] != 1:
#         perp_vector1 = np.cross(sun_direction, [0, 0, 1])
#     else:
#         perp_vector1 = np.cross(sun_direction, [0, 1, 0])
#     perp_vector1 /= np.linalg.norm(perp_vector1)
#     perp_vector2 = np.cross(sun_direction, perp_vector1)
#     half_width = width / 2
#     half_height = height / 2
#     v1 = half_width * perp_vector1 + half_height * perp_vector2
#     v2 = -half_width * perp_vector1 + half_height * perp_vector2
#     v3 = -half_width * perp_vector1 - half_height * perp_vector2
#     v4 = half_width * perp_vector1 - half_height * perp_vector2
#     return [v1, v2, v3, v4]


def calculate_centered_rectangle_vertices(sun_x, sun_y, sun_z, width, height):
    sun_direction = np.array([sun_x, sun_y, sun_z])
    sun_direction /= np.linalg.norm(sun_direction)

    # Pitch: Angle between the sun direction projection on YZ plane and Y-axis

    pitch = -np.arctan2(sun_direction[1], sun_direction[2])

    # Apply pitch rotation (around X-axis)
    rot_x = np.array([[1, 0, 0],
                      [0, np.cos(pitch), -np.sin(pitch)],
                      [0, np.sin(pitch), np.cos(pitch)]])
    sun_direction_pitch_rotated = np.dot(rot_x, sun_direction)

    # Yaw: Angle between the sun direction projection on XY plane and X-axis
    yaw =180-np.arctan2(sun_direction_pitch_rotated[0], sun_direction_pitch_rotated[2])

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

# Location details (Los Angeles, USA)
latitude = 34.05
longitude = -118.25

# Initialize plot outside the loop
plt.ion()  # Turn on interactive mode
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Continuously update the plot
while True:
    # Get current date and time
    current_time = datetime.now()

    site = Location(latitude, longitude, 'America/Los_Angeles', 93, 'Los Angeles')
    site_tz = pytz.timezone('America/Los_Angeles')
    end_time = pd.Timestamp.now(tz=site_tz)
    start_time = end_time - pd.Timedelta(hours=5)
   # times = pd.date_range(start=start_time, end=end_time, freq='H', tz=site_tz)

    solpos = solarposition.get_solarposition(end_time, site.latitude, site.longitude, site.altitude)

    
    solar_zenith = solpos['zenith'].iloc[0]
    solar_azimuth = solpos['azimuth'].iloc[0]

    # Convert to 3D coordinates
    x, y, z = spherical_to_cartesian(solar_zenith, solar_azimuth)

    # Clear previous data
    ax.clear()

    # Redraw the elements

    # Equator line
   # Equator line drawn clockwise
    u_eq = np.linspace(0, 2 * np.pi, 100)  
    ax.plot(np.cos(u_eq), np.sin(u_eq), 0, color="b", alpha=0.3)

    # Define compass points (updated for clockwise azimuth)
    compass_points = {'N': 0, 'E': 270, 'S': 180, 'W': 90}

    # Label compass points
    for point, angle in compass_points.items():
        angle_rad = np.radians(angle)
        label_x = np.cos(angle_rad)
        label_y = np.sin(angle_rad)
        ax.text(label_x, label_y, 0, point, color="red", fontsize=12, ha='center', va='center')

    # Four dome lines (updated for clockwise azimuth)
    v_dom = np.linspace(0, np.pi, 100)
    for angle in [0, 270, 180, 90]:
        angle_rad = np.radians(angle)
        ax.plot(np.cos(angle_rad) * np.sin(v_dom), np.sin(angle_rad) * np.sin(v_dom), np.cos(v_dom), color="b", alpha=0.3)

    # Sun's position
    ax.scatter(x, y, z, color='yellow', s=100)

    # Line to sun's position
    ax.plot([0, x], [0, y], [0, z], color='red')

    # Rectangle
    rectangle_width = 0.2
    rectangle_height = 0.4
    rectangle_vertices = calculate_centered_rectangle_vertices(x, y, z, rectangle_width, rectangle_height)
    rectangle = Poly3DCollection([rectangle_vertices], color='cyan', alpha=0.6)
    ax.add_collection3d(rectangle)

    # Axis labels
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')

    # Degree angles for azimuth and elevation
    for angle in range(0, 360, 30):
        ax.text(np.cos(np.radians(angle)), np.sin(np.radians(angle)), 0, f"{angle}°", color="green")
    for angle in range(0, 180, 30):
        ax.text(0, np.sin(np.radians(angle)), np.cos(np.radians(angle)), f"{angle}°", color="blue")

    # Title
    ax.set_title('Live Sun Position on Spherical Coordinates')

    plt.draw()
    plt.pause(60)  # Pause for 60 seconds
