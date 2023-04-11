'''
彩色图像的直方图均衡化操作, 需要将原有的色彩空间转换为包含亮度的色彩通道。 
HSV 是一种描述颜色的方式，它表示颜色的三个属性：色相（Hue）、饱和度（Saturation）、亮度（Value）
'''
import cv2
import matplotlib.pyplot as plt
# flags 0 表示灰度图像，1 原始图像
img = cv2.imread('./dataset/data/sunrise.jpg', flags=1)

cv2.imshow('img', img)
# imread 读取的图片只是 BGR 格式的，没有亮度选项，需要将色彩空间转换为 HSV 格式的色彩空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# 重新赋值给原来的通道, 否则使用直接使用 cv2.equalizeHist(hsv[:,:, 2]) 只能得到一个灰度图像，因为使用切片取出的数据只是一个2维数
# 所以必须使用切片重新赋值给 hsv 
hsv[:, :, 2] = cv2.equalizeHist(hsv[:,:, 2])
# 将 HSV 转换为 BGR 格式
hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

cv2.imshow('hsv', hsv)


cv2.waitKey()
cv2.destroyAllWindows()