import numpy as np
import cv2
from matplotlib import pyplot as plt


# # SIFT
img1 = cv2.imread('sift1.jpg',0) # queryImage
img2 = cv2.imread('sift2.jpg',0) # trainImage

# Initiate SIFT detector
sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,img1,flags=2)

plt.imshow(img3),plt.show()

# # SURF
# from matplotlib import pyplot as plt
# img =cv2.imread('images/prilly4.jpg',0)
# # img=cv2.SURF(400)
# surf= cv2.xfeatures2d.SURF_create()
# kp1,des1= surf.detectAndCompute(img,None)
# img2 = cv2.drawKeypoints(img,kp1,None,(255,0,0),4)
# plt.imshow(img2),plt.show()