'''
    边沿检测
'''
import cv2

img = cv2.imread('./dataset/data/lily.png', 0)

cv2.imshow('img', img)
# src 输入图像，可以是灰度图像或彩色图像，数据类型为uint8或float32。 
# ddepth 输出图像的深度，如果为-1，表示输出图像深度与输入图像相同。
# dx 输出图像的深度，如果为-1，表示输出图像深度与输入图像相同。
# dy 表示竖直方向上的导数阶数，0、1、2分别表示不求导、一阶导、二阶导。 
# Sobel算子的大小，必须为1、3、5、7等奇数，如果不指定，则默认为3。
sobel = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=1, ksize=5)

cv2.imshow("sobel", sobel)

# laplacain
laplacain = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow("laplacain", laplacain)

# canny
# image：输入图像，必须是单通道灰度图像，数据类型为uint8或float32。
# threshold1：第一个阈值，用于控制边缘的强度，较小的值会导致更多的边缘被检测到。
# threshold2：第二个阈值，用于控制边缘的强度，较大的值会导致更少的边缘被检测到
canny = cv2.Canny(image=img, threshold1=50, threshold2=360)
cv2.imshow("canny", canny)



cv2.waitKey()
cv2.destroyAllWindows()