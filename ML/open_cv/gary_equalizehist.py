'''
    直方图均衡化，
'''
import cv2
import matplotlib.pyplot as plt
# flags 0 表示灰度图像，1 原始图像
img = cv2.imread('./dataset/data/sunrise.jpg', flags=0)
print(img.shape)
cv2.imshow('img', img)

img_equ = cv2.equalizeHist(img)

cv2.imshow('equ', img_equ)

# 使用 plt 画出子图
plt.subplot(1,2, 1)
# 画出直方图， 直方图只能使用一维数组。 bins 直方图中的柱子数量，  range 表示直方图数值范围的最小值和最大值。
plt.hist(img.ravel(), bins=256, range=(0, 256))

plt.subplot(1,2,2)
# 画出直方图， 直方图只能使用一维数组。 bins 直方图中的柱子数量，  range 表示直方图数值范围的最小值和最大值。
plt.hist(img_equ.ravel(), bins=256, range=(0, 256))

# plt.show()

cv2.waitKey()
cv2.destroyAllWindows()