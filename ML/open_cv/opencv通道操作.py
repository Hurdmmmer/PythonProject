'''
图像通道操作， 彩色图片为3通道， 0 蓝色通道，1 绿色通道，2 红色通道
'''
import cv2

img = cv2.imread('./dataset/data/opencv.png')
print(img.shape)

cv2.imshow('img', img)

# 取出彩色图片的第0个通道，然后显示, 需要注意的是，切片取出后。数据的维度为 2 了 
# 图片切片的原理是，所有行，所有高，通道数0
img_b = img[:, :, 0]
print(img_b.shape)
cv2.imshow('img_b', img_b)
# 切片赋值操作，将原来 0 通道中的树改为 0
img[:, :, 0] = 0
cv2.imshow('b0', img)

img[:, :, 1] = 0
cv2.imshow('b0g0', img)



cv2.waitKey()
cv2.destroyAllWindows()
