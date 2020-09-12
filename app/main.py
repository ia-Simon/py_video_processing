from interfaces.video_capture import VideoCapture
import sys


if __name__ == "__main__":
    cap = VideoCapture("Ip stream")

    if (option:="--from_stream") in sys.argv:
        cap.ip_stream(sys.argv[sys.argv.index(option) + 1], portrait_mode=True)
    elif "--screen" in sys.argv:
        cap.screen()
