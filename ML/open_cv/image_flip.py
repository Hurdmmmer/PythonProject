'''
    图像的镜像操作
'''
import cv2

img = cv2.imread('./dataset/data/lena.jpg')

cv2.imshow('img', img)

img0 = cv2.flip(img, 0)
cv2.imshow('img0', img0)

img1 = cv2.flip(img, 1)
cv2.imshow('img1', img1)

cv2.waitKey()
cv2.destroyAllWindows()