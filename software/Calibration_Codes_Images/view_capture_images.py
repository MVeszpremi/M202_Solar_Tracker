import cv2
import tkinter as tk
from PIL import Image, ImageTk

class WebcamApp:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)

        # Initialize webcam
        self.video_source = 0
        self.vid = cv2.VideoCapture(self.video_source)

        # Scale factor
        self.scale_factor = 2

        # Adjust the size of the window
        self.window_width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH) / self.scale_factor)
        self.window_height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT) / self.scale_factor)
        self.window.geometry(f"{self.window_width + 100}x{self.window_height}")

        # Create a canvas that can fit the scaled video source size
        self.canvas = tk.Canvas(window, width=self.window_width, height=self.window_height)
        self.canvas.pack(side=tk.LEFT)

        # Button that lets the user take a snapshot
        self.btn_snapshot = tk.Button(window, text="Snapshot", command=self.snapshot)
        self.btn_snapshot.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Start the video process
        self.update_video()

    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.read()
        if ret:
            # Resize the frame before saving
            resized_frame = cv2.resize(frame, (self.window_width, self.window_height))
            cv2.imwrite("frame-" + str(self.vid.get(cv2.CAP_PROP_POS_FRAMES)) + ".png", cv2.cvtColor(resized_frame, cv2.COLOR_RGB2BGR))

    def update_video(self):
        # Get a frame from the video source
        ret, frame = self.vid.read()
        if ret:
            # Resize the frame for display
            resized_frame = cv2.resize(frame, (self.window_width, self.window_height))
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(10, self.update_video)

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()

# Create a window and pass it to the WebcamApp class
root = tk.Tk()
app = WebcamApp(root, "Tkinter and OpenCV")
root.mainloop()
