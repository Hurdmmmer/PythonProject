'''
    先腐蚀，在膨胀， 是对图片的开运算
    先膨胀，后腐蚀， 是对图片的闭运算
'''

import cv2
import numpy as np

# 读取图片
origin = cv2.imread('./1.png', 0)
origin1 = cv2.imread('./1.png', 1)

size = origin.shape
img = origin[:size[0]-60, :]

# res = cv2.cvtColor(origin, cv2.COLOR_BGR2GRAY)

t, res = cv2.threshold(img, 175, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('tt', res)

# 对图像进行腐蚀， 用于收敛毛刺
# iterations 设置腐蚀次数，用于控制腐蚀效果
# kernel 腐蚀核大小，用于控制腐蚀的效果
kernal = np.ones((3, 3), np.uint8)
res1 = cv2.erode(res, kernel=kernal, iterations=4)
# cv2.imshow('res1', res1)

kernal = np.ones((3, 3), np.uint8)
# 对数据进行膨胀
res2 = cv2.dilate(res1, kernel=kernal)
# cv2.imshow('res2', res2)

res = cv2.subtract(res2, res1)
# cv2.imshow('res3', res)

contours, hierarchy = cv2.findContours(res, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# for i in range(len(contours)):
#     mom = cv2.moments(contours[i]) #计算中心矩
#     pt = (int(mom['m10'] / mom['m00']), int(mom['m01'] / mom['m00']))  # 使用前三个矩m00, m01和m10计算重心
    
#     cv2.putText(origin1, str(i), (pt[0], pt[1]), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 1, 8, 0);#加坐标

# cv2.drawContours(origin1, contours, -1, (0,0,255), 1)

# perimeter = cv2.arcLength(contours[28], True)
# area = cv2.contourArea(contours[28])
# print(perimeter, area)

# perimeter1 = cv2.arcLength(contours[26], True)
# area1 = cv2.contourArea(contours[26])
# print(perimeter1, area1)


# 遍历每个轮廓
for contour in contours:
    # 如果轮廓长度小于100，不考虑 
    if len(contour) < 20:
        continue

    # 计算轮廓的周长和面积
    perimeter = cv2.arcLength(contour, True)
    area = cv2.contourArea(contour)

    # 如果轮廓周长或面积不在预定范围内，不考虑
    if perimeter < 240 or perimeter > 300 or area < 1600 or area > 2700:
        continue

    # 进一步检查轮廓的形状， 拟合多边形，必须是闭合的多边形 
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)

    # 如果轮廓具有四条边（即矩形），则将其视为可能的缺口
    if len(approx) >= 4:
        # 求出缺口的位置
        x, y, w, h = cv2.boundingRect(contour)
        # 在原始图像中绘制矩形
        cv2.rectangle(origin1, (x, y), (x+w, y+h), (0,0,255), 2)

cv2.imshow('img', origin1)

cv2.waitKey()
cv2.destroyAllWindows()
