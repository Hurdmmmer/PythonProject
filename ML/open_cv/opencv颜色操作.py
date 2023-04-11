'''
    opencv 对图像的颜色的操作
'''
import cv2

# 读取图像
img = cv2.imread('./dataset/data/Linus.png')
# 输出的结果为 高度，宽度，通道数
print(img.shape)

# 将彩色图像转换为灰度图像
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


cv2.imshow('RGB', img)
cv2.imshow('Gray', img_gray)

cv2.waitKey()
cv2.destroyAllWindows()