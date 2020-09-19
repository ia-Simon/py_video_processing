import cv2
import numpy as np
from functools import partial

class ColorDetection:
    hue_min = 0
    hue_max = 179
    sat_min = 0
    sat_max = 255
    val_min = 0
    val_max = 255

    def grid_2x2(self, imgs, *, scale=1):   
        rows = []
        for line in imgs:
            rows.append(np.hstack(tuple([np.stack([img] * 3, axis=-1) 
                if len(img.shape) == 2 else img for img in line])))
        grid = np.vstack(tuple(rows))
        return cv2.resize(grid, tuple([int(measure*scale) for measure in grid.shape[1::-1]]))
    
    def set_attr(self, value, *, attr):
        setattr(self, attr, value)


    def detect_color(self, img_path: str, panel_scale: float = 1):
        cv2.namedWindow('HSV Control', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('HSV Control', 640, 200)
        cv2.createTrackbar('Hue Min: ', 'HSV Control', self.hue_min, 179, partial(self.set_attr, attr='hue_min'))
        cv2.createTrackbar('Hue Max: ', 'HSV Control', self.hue_max, 179, partial(self.set_attr, attr='hue_max'))
        cv2.createTrackbar('Sat Min: ', 'HSV Control', self.sat_min, 255, partial(self.set_attr, attr='sat_min'))
        cv2.createTrackbar('Sat Max: ', 'HSV Control', self.sat_max, 255, partial(self.set_attr, attr='sat_max'))
        cv2.createTrackbar('Val Min: ', 'HSV Control', self.val_min, 255, partial(self.set_attr, attr='val_min'))
        cv2.createTrackbar('Val Max: ', 'HSV Control', self.val_max, 255, partial(self.set_attr, attr='val_max'))

        img = cv2.imread(img_path)
        img_HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        while True:
            lower_HSV = np.array([self.hue_min, self.sat_min, self.val_min])
            upper_HSV = np.array([self.hue_max, self.sat_max, self.val_max])
            mask = cv2.inRange(img_HSV, lower_HSV, upper_HSV)

            img_masked = cv2.bitwise_and(img, img, mask=mask)

            stack = self.grid_2x2([[img, img_HSV], [mask, img_masked]], scale=panel_scale)

            cv2.imshow("Main Panel", stack)

            if cv2.waitKey(1) == 27:
                break

        cv2.destroyAllWindows()