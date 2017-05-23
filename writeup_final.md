##Writeup Template
###RS
---

**Advanced Lane Finding Project**

The goals / steps of this project are the following:

* Compute the camera calibration matrix and distortion coefficients given a set of chessboard images.
* Apply a distortion correction to raw images.
* Use color transforms, gradients, etc., to create a thresholded binary image.
* Apply a perspective transform to rectify binary image ("birds-eye view").
* Detect lane pixels and fit to find the lane boundary.
* Determine the curvature of the lane and vehicle position with respect to center.
* Warp the detected lane boundaries back onto the original image.
* Output visual display of the lane boundaries and numerical estimation of lane curvature and vehicle position.

[//]: # (Image References)

[image1]: ./output_images/final.jpg "final"
[image2]: ./output_images/threshold.jpg "threshold"
[image3]: ./output_images/undistort.jpg "undistort"
[image4]: ./output_images/warp.jpg "warp"

---
###Writeup / README

###Camera Calibration

####1. Briefly state how you computed the camera matrix and distortion coefficients. Provide an example of a distortion corrected calibration image.

The code for this step is contained in the lesson package (lesson folder) and is in the file 'unidstort.py' as the 'undistort' class.

Using the provided camera calibration images, the code iterates through finding the chessboard corners and its coordinates (with the find_corners function within the undistort class). It stores the results in an array and passes them to open cv2's calibrateCamera function to calibrate the camera. Below is an example.

![unidstort][image3]

###Pipeline (single images)

####2. Describe how (and identify where in your code) you used color transforms, gradients or other methods to create a thresholded binary image.  Provide an example of a binary image result.

I used a combination of color and gradient thresholds to generate a binary image (the thresholding steps can be found in the lesson package in the Gradient_Threshold class).

Here is an example.

![threshold][image2]

####3. Describe how (and identify where in your code) you performed a perspective transform and provide an example of a transformed image.

The code for my perspective transform can be found in the lesson package under the warp class. It leverages the cv2.getPerspectiveTransform() method and the source and destination points are as follows: [580, 460],[700, 460],[1040, 680],[260, 680] ;
[260, 0],[1040, 0],[1040, 720],[260, 720]

Here is an example

![warp][image4]

####4. Describe how (and identify where in your code) you identified lane-line pixels and fit their positions with a polynomial?

In the lesson package under the polynomialfit class there exists a function called sliding_n_fit. The method takes a warped binary image and starts by computing a histogram on the lower half of the image to find an approximate position of each line.
It then runs a sliding window vertically to try and detect the center of each lane line. Finally, using numpy's polyfit method and the positions found in the previous step, polylines for each lane are computed.


####5. Describe how (and identify where in your code) you calculated the radius of curvature of the lane and the position of the vehicle with respect to center.

In the lesson package under the polynomialfit class there exists a function called measuring_curvature. It performs two calculations. 1) Using the computed polylines along with the estimated lane width of approximately 3.7m,  a real-world lane curvature is computed. 2) Also, the position of the car with respect to the lane is computed as the difference between the center of the lane and the center of the image.

####6. Provide an example image of your result plotted back down onto the road such that the lane area is identified clearly.

Finally, in the lesson package is a class called draw. This class contains a method called drawing which constructs a polygon using the curves (polylines) to warp back the result using cv2.getPerspectiveTransform(dst, src).

Here is an example

![final][image1]

---

###Pipeline (video)

####1. Provide a link to your final video output.  Your pipeline should perform reasonably well on the entire project video (wobbly lines are ok but no catastrophic failures that would cause the car to drive off the road!).

Here's a [link to my video result](./project_video_done.mp4)

---

###Discussion

####1. Briefly discuss any problems / issues you faced in your implementation of this project.  Where will your pipeline likely fail?  What could you do to make it more robust?

No major issues occurred, a majority of the code was taken (and only slightly modified) from the lesson.

The current implementation would most likely fail in very dark and very bright images (images where it would be difficult to extract white and yellow lanes). It may also need to be slightly modified to handle other colored lane lines. And would obviously fail if lane lines were missing or very worn.

One thought for improving, would be to optimize to handle more lane line colors and differing light environments.
