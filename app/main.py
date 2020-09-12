import cv2
import numpy as np
from mss import mss

window_name = "Test Window"

def screen():
    cv2.namedWindow(window_name)

    monitor = {'top': 0, 'left': 0, 'width': 1360, 'height': 768}
    sct = mss()

    while True:
        img = sct.grab(monitor)
        frame = np.array(img)
        frame = cv2.resize(frame, tuple([int(measure*0.8) for measure in frame.shape[1::-1]]))
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()

def camera():
    cv2.namedWindow(window_name)
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        cap.open()
        ret, frame = cap.read()
    print(ret)

    while ret:
        ret, frame = cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2.imshow(window_name, frame)
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
    
if __name__ == "__main__":
    choice = input("0 for screen recording, 1 for camera recording\n> ") 
    if choice == '0':
        screen()
    elif choice == '1':
        camera()
    else:
        print("Option not found")
