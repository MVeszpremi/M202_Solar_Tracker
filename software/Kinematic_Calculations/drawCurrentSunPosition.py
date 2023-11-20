import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import pvlib
from datetime import datetime

# Function to convert spherical to cartesian coordinates
def spherical_to_cartesian(azimuth, elevation):
    r = 1  # unit sphere
    azimuth_rad = np.radians(azimuth)
    elevation_rad = np.radians(90 - elevation)  # Convert to colatitude
    x = r * np.sin(elevation_rad) * np.cos(azimuth_rad)
    y = r * np.sin(elevation_rad) * np.sin(azimuth_rad)
    z = r * np.cos(elevation_rad)
    return x, y, z

# Function to calculate rectangle vertices
def calculate_centered_rectangle_vertices(x, y, z, width, height):
    sun_direction = np.array([x, y, z])
    sun_direction /= np.linalg.norm(sun_direction)
    if sun_direction[2] != 1:
        perp_vector1 = np.cross(sun_direction, [0, 0, 1])
    else:
        perp_vector1 = np.cross(sun_direction, [0, 1, 0])
    perp_vector1 /= np.linalg.norm(perp_vector1)
    perp_vector2 = np.cross(sun_direction, perp_vector1)
    half_width = width / 2
    half_height = height / 2
    v1 = half_width * perp_vector1 + half_height * perp_vector2
    v2 = -half_width * perp_vector1 + half_height * perp_vector2
    v3 = -half_width * perp_vector1 - half_height * perp_vector2
    v4 = half_width * perp_vector1 - half_height * perp_vector2
    return [v1, v2, v3, v4]

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

    # Get solar position
    solpos = pvlib.solarposition.get_solarposition(current_time, latitude, longitude)

    # Sun's azimuth and altitude
    azimuth = solpos['azimuth'].iloc[0]
    altitude = solpos['apparent_elevation'].iloc[0]

    # Convert to 3D coordinates
    x, y, z = spherical_to_cartesian(azimuth, altitude)

    # Clear previous data
    ax.clear()

    # Redraw the elements

    # Equator line
    u_eq = np.linspace(0, 2 * np.pi, 100)
    ax.plot(np.cos(u_eq), np.sin(u_eq), 0, color="b", alpha=0.3)

    # Four dome lines
    v_dom = np.linspace(0, np.pi, 100)
    for angle in [0, 90, 180, 270]:
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
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_zlabel('')

    # Degree angles for azimuth and elevation
    for angle in range(0, 360, 30):
        ax.text(np.cos(np.radians(angle)), np.sin(np.radians(angle)), 0, f"{angle}°", color="green")
    for angle in range(0, 180, 30):
        ax.text(0, np.sin(np.radians(angle)), np.cos(np.radians(angle)), f"{angle}°", color="blue")

    # Title
    ax.set_title('Live Sun Position on Spherical Coordinates')

    plt.draw()
    plt.pause(60)  # Pause for 60 seconds
