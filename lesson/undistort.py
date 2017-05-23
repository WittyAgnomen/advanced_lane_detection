#Distortion correction
import cv2
import numpy as np
import glob


class Undistort:
    def __init__(self):
        try:
            self.objpoints = np.load('CBCorners/objpoints.npy')
            self.imgpoints = np.load('CBCorners/imgpoints.npy')
            self.shape = tuple(np.load('CBCorners/shape.npy'))
        except:
            self.objpoints = None
            self.imgpoints = None
            self.shape = None
            self.find_corners() #objpoints, imgpoints, and shape should be full now

        ret, self.mtx, self.dist, self.rvecs, self.tvecs = cv2.calibrateCamera(self.objpoints, self.imgpoints,
                                                                               self.shape,
                                                                               None, None)

    def undist(self, img):
        return cv2.undistort(img, self.mtx, self.dist, None, self.mtx)

    def find_corners(self):
        images = glob.glob('camera_cal/calibration*.jpg')
        base = np.zeros((6 * 9, 3), np.float32)
        base[:, :2] = np.mgrid[0:9, 0:6].T.reshape(-1, 2)
        self.objpoints = []
        self.imgpoints = []
        self.shape = None

        for i in images:
            img = cv2.imread(i)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            if self.shape is None:
                self.shape = gray.shape[::-1]

            print('Finding chessboard corners') #for verifying method is running
            ret, corners = cv2.findChessboardCorners(gray, (9, 6), None)

            if ret:
                self.objpoints.append(base)
                self.imgpoints.append(corners)

        np.save('CBCorners/objpoints', self.objpoints)
        np.save('CBCorners/imgpoints', self.imgpoints)
        np.save('CBCorners/shape', self.shape)
