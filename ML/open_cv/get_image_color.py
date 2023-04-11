'''
    提取图片中的颜色
'''
import cv2
import numpy as np

img = cv2.imread('./dataset/data/opencv.png')

cv2.imshow('img', img)
# 使用 cv2 inrang 方法提取图片
# 1. 转换图片到 hsv 格式
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 2. 匹配指定的颜色区间，获取该区间的掩码
# 设置 HSV 色彩空间中指定颜色的区间
color_min_range = np.array([110, 50, 50])
color_max_range = np.array([130, 255, 255])
# 它的作用是将一副 RGB 或 HSV 图像根据给定的上下界阈值，生成值为 0 或 255 的二值化图像。
# 具体来说，它会把在阈值范围内的像素点变成白色，其它取值范围的点则变成黑色。
mask = cv2.inRange(hsv, color_min_range, color_max_range)
print(mask.shape)
cv2.imshow('mask', mask)

# 3. 在原始图片中进行位与操作(只要非0的数据)，提取图片
bule_color = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('bule', bule_color)

cv2.waitKey()
cv2.destroyAllWindows()