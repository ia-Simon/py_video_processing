import cv2
import numpy as np
from mss import mss

class VideoCapture:
    def __init__(self, window_name: str):
        self.window_name = window_name

    def screen(self):
        cv2.namedWindow(self.window_name)

        monitor = {'top': 0, 'left': 0, 'width': 1360, 'height': 768}
        sct = mss()

        while True:
            img = sct.grab(monitor)
            frame = np.array(img)
            frame = cv2.resize(frame, tuple([int(measure*0.8) for measure in frame.shape[1::-1]]))
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imshow(self.window_name, frame)
            if cv2.waitKey(1) == 27:
                break

        cv2.destroyAllWindows()

    def ip_stream(self, ip_address: str, *, portrait_mode: bool):
        cap = cv2.VideoCapture(ip_address)
        cv2.namedWindow(self.window_name)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.resize(frame, tuple([int(measure*0.3) for measure in frame.shape[1::-1]]))
            if portrait_mode:
                frame = np.rot90(frame, k=-1, axes=(0, 1))
            # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.imshow(self.window_name, frame)
            if cv2.waitKey(1) == 27:
                break

        cap.release()
        cv2.destroyAllWindows()