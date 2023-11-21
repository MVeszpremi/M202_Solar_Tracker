import DataPlotter
import SerialCommunication
import SphericalDiagramUpdater

class Main:
    def __init__(self):
        self.spherical_updater = SphericalDiagramUpdater(latitude=34.05, longitude=-118.25)
        self.serial_communication = SerialCommunication(desired_rotation_y=100, desired_rotation_x=100)
        self.data_plotter = DataPlotter()

    def start_system(self):
        self.spherical_updater.start()
        self.serial_communication.start()

if __name__ == "__main__":
    main_system = Main()
    main_system.start_system()
