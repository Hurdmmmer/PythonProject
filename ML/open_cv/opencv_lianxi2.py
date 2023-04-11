'''
    open cv 坏点检测
'''
import cv2
img = cv2.imread('./dataset/data/CPU3.png')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

t, binary = cv2.threshold(img, 170, 255, cv2.THRESH_BINARY)


cv2.imshow('img', binary)
cv2.waitKey()
cv2.destroyAllWindows()