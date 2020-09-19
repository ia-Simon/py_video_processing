from interfaces.video_capture import VideoCapture
from interfaces.color_detection import ColorDetection
import sys


if __name__ == "__main__":
    cap = VideoCapture("Ip stream")
    detector = ColorDetection()

    if (option:="--from_stream") in sys.argv:
        cap.ip_stream(
            sys.argv[sys.argv.index(option) + 1], 
            portrait_mode=True if "--portrait" in sys.argv else False
        )
    elif "--screen" in sys.argv:
        cap.screen()
    elif (option:="--color_detection") in sys.argv:
        detector.detect_color(
            sys.argv[sys.argv.index(option) + 1],
            float(sys.argv[sys.argv.index("--scale") + 1]) if "--scale" in sys.argv else 1
        )
