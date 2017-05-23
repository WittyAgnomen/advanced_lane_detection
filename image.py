#file that performs advance lane detection
#import libs
import cv2
from moviepy.video.io.VideoFileClip import VideoFileClip as vc
from scipy import misc
#import classes from lesson package
from lesson.draw import draw
from lesson.gradient_threshold import Gradient_Threshold
from lesson.polynomialfit import PolynomialFit
from lesson.undistort import Undistort
from lesson.warp import Warp

draw=draw()
gt=Gradient_Threshold()
pf=PolynomialFit()
ud=Undistort()
warp=Warp()

def main():
    video_in='project_video.mp4'
    video_out='project_video_done.mp4'
    start=0 #secs to start clip at
    end=50 #secs to end clip at
    clip = vc(video_in).subclip(start, end)
    proc_clip=clip.fl_image(process_image)
    proc_clip.write_videofile(video_out, audio=False)

def process_image(frame):

    #call undistort
    ud_img = ud.undist(frame)
    #misc.imsave('output_images/undistort.jpg', ud_img) #save image
    #call threshold
    img = gt.threshold(ud_img)
    #misc.imsave('output_images/threshold.jpg', img) #save image
    # call warp
    img = warp.dowarp(img)
    #misc.imsave('output_images/warp.jpg', img) #save image

    left_fit, right_fit = pf.sliding_n_fit(img)
    #draw lanes
    img = draw.drawing(ud_img, left_fit, right_fit, warp.Minv)
    #misc.imsave('output_images/final.jpg', img) #save image

    lane_curve, car_pos = pf.measuring_curvature(img)

    if car_pos > 0:
        car_pos_text = '{}m right of center'.format(car_pos)
    else:
        car_pos_text = '{}m left of center'.format(abs(car_pos))

    #display car location and lane curvature
    cv2.putText(img, "lane curve: {}m".format(lane_curve.round()), (700, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
                color=(255, 255, 255), thickness=2)
    cv2.putText(img, "The car is {}".format(car_pos_text), (700, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, color=(255, 255, 255),
                thickness=2)

    return img

if __name__ == '__main__':
    main()
