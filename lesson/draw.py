# draw lines #function constructed from lesson section 'tips and tricks'
import cv2
import numpy as np


class draw:
    def drawing(self, img, left_fit, right_fit, Minv):
        # Create an image to draw the lines on
        warp = np.zeros_like(img).astype(np.uint8)

        ploty = np.linspace(0, img.shape[0] - 1, img.shape[0])
        #polynomials
        left_fitx = left_fit[0] * ploty ** 2 + left_fit[1] * ploty + left_fit[2]
        right_fitx = right_fit[0] * ploty ** 2 + right_fit[1] * ploty + right_fit[2]

        # Recast the x and y points into usable format for cv2.fillPoly()
        pts_left = np.array([np.transpose(np.vstack([left_fitx, ploty]))])
        pts_right = np.array([np.flipud(np.transpose(np.vstack([right_fitx, ploty])))])
        pts = np.array((np.hstack((pts_left, pts_right))), dtype=np.int32)

        # Draw the lane onto the warped blank image
        cv2.fillPoly(warp, np.int_([pts]), (0,255, 0))

        # Warp the blank back to original image space using inverse perspective matrix (Minv)
        newwarp = cv2.warpPerspective(warp, Minv, (img.shape[1], img.shape[0]))
        # Combine the result with the original image
        result = cv2.addWeighted(img, 1, newwarp, 0.3, 0)
        return result
