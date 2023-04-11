'''
    opencv 综合案例，将倾斜的纸扶正,
    当前的 demo 中直接使用二值化无法将纸张的边缘显示清晰。
    所以我们使用边缘检测来强化图片的边缘
'''
import cv2
import numpy as np

img = cv2.imread('./dataset/data/paper.jpg')
origin1 = cv2.imread('./dataset/data/paper.jpg')


img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 无法使用二值化检测纸张边缘
# t, binary = cv2.threshold(img, thresh=200,maxval=255, type =cv2.THRESH_BINARY_INV)
# kernel = np.ones((3,3), np.uint8)
# sobel = cv2.Sobel(img, cv2.CV_64F, dx=1,dy=1,ksize=5)
# cv2.imshow('img', sobel)

# laplacain = cv2.Laplacian(img, cv2.CV_64F)
# cv2.imshow("laplacain", laplacain)
# 膨胀
# img = cv2.dilate(img, (2,2))

# canny 强化图片的轮廓
canny = cv2.Canny(image=img, threshold1=100, threshold2=360)

contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

result = None
if len(contours) > 0:
    # 根据面积排序
    for cnt in contours:
            # 对当前匹配的轮廓进行多边形匹配。
            approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
            if len(approx) == 4 and cv2.contourArea(cnt) > 100:
                result = approx
                # break
            
# 画出匹配的点位

for peak in result:
    point = peak[0]
    cv2.circle(origin1, tuple(point), 10, (0,0,255))
    




cv2.imshow("canny", origin1)
cv2.waitKey()
cv2.destroyAllWindows()