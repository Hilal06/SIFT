import numpy as np
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('images/test-2.jpg')
img2 = cv2.imread('images/test-image.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
sift = cv2.xfeatures2d.SIFT_create()

# kp = sift.detect(gray, None)
# kp_img2 = sift.detect(gray2, None)
#
# des = sift.compute(image=gray, keypoints=kp)
# des2 = sift.compute(image=gray2, keypoints=kp_img2)

kp, des = sift.detectAndCompute(gray, None)
kp2, des2 = sift.detectAndCompute(gray2, None)

img = cv2.drawKeypoints(gray, kp, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)
img2 = cv2.drawKeypoints(gray2, kp2, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT, outImage=None)


cv2.imwrite('sift_res_img1.jpg', img)
cv2.imwrite('sift_res_img2.jpg', img2)

# des_img1 = des[1]
# des_img2 = des2[1]

# # brt = cv2.BFMatcher()
# brt = cv2.BFMatcher()
# matches = brt.knnMatch(des, des2, k=2)
# # matches = brt.match(des, des2)
# # matches = sorted(matches, key=lambda x: x.distance)
#
# good = []
# for m, n in matches:
#     if m.distance < 0.8 * n.distance:
#         good.append([m])
#
# # img_res = cv2.drawMatchesKnn(img, kp, img2, kp_img2, good, None)
# img_res = cv2.drawMatchesKnn(img, kp, img2, kp2, good[:20], None, flags=2)

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

