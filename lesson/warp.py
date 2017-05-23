#Perspective transform
#pretty much generated code form 'How I did it' section in lesson
import cv2
import numpy as np

class Warp:
    def __init__(self):
        src = np.float32([[580, 460],[700, 460],[1040, 680],[260, 680],])

        dst = np.float32([[260, 0],[1040, 0],[1040, 720],[260, 720],])

        self.M = cv2.getPerspectiveTransform(src, dst)
        self.Minv = cv2.getPerspectiveTransform(dst, src)

    def dowarp(self, img):
        return cv2.warpPerspective(img, self.M, (img.shape[1], img.shape[0]), flags=cv2.INTER_LINEAR)

    def unwarp(self, img):
        return cv2.warpPersective(img, self.Minv, (img.shape[1], img.shape[0]), flags=cv2.INTER_LINEAR)
