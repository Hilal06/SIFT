import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('images/test-2.jpg')
img2 = cv2.imread('images/test-image.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()


kp, des = sift.detectAndCompute(gray, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

img = cv2.drawKeypoints(gray, kp, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)
img2 = cv2.drawKeypoints(gray2, kp2, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)


cv2.imwrite('sift_res_img1.jpg', img)
cv2.imwrite('sift_res_img2.jpg', img2)



FLANN_INDEX_KDTREE = 0
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv2.FlannBasedMatcher(index_params, search_params)

matches = flann.knnMatch(des, des2, k=2)

# Need to draw only good matches, so create a mask
matchesMask = [[0, 0] for i in range(len(matches))]

# ratio test as per Lowe's paper
for i, (m, n) in enumerate(matches):
    if m.distance < 0.8*n.distance:
        matchesMask[i] = [1, 0]

draw_params = dict(
                   singlePointColor=(255, 0, 0),
                   matchesMask=matchesMask,
                   flags=0)

img_res = cv2.drawMatchesKnn(gray, kp, gray2, kp2, matches, None, **draw_params)

plt.imshow(img_res)
plt.show()
cv2.destroyAllWindows()


# img = cv2.imread('images/3x4.jpg')
# gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# #extracts SIFT features from images
# sift = cv2.xfeatures2d.SIFT_create()
# kp = sift.detect(gray,None)
#
# img=cv2.drawKeypoints(gray,kp,img,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
#
# cv2.imwrite('sift_keypoints3.jpg',img)