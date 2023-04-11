'''
    图像卷积, 使用指定的卷积核显示斑马的垂直条纹，和水平条纹
'''
from scipy import signal # 做卷积
import imageio.v2 as imageio
import numpy as np
import matplotlib.pyplot as plt



img = imageio.imread("/home/jansen/PythonProject/ML/data_test/DeepLearning/dataset/data/zebra.png")
gray_img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

# 垂直方向的卷积核
flt0 = np.array([[-1,0,1],
                 [-2,0,2],
                 [-1,0,1]])
# 水平方向的卷积核
flt1 = np.array([[1,2,1],
                 [0,0,0],
                 [-1,-2,-1]])


# 开始卷积
# 参数一：灰度图像
# 参数二: 卷积核
# 参数三：？
# 参数四：同纬卷积，结果输出的维度和原始图片一样
conv1 = signal.convolve2d(gray_img, flt0, boundary='symm', mode="same").astype('int32')

conv2 = signal.convolve2d(gray_img, flt1, boundary='symm', mode="same").astype('int32')

plt.figure("2D")
plt.subplot(1, 3, 1)

plt.imshow(gray_img, cmap='gray')
plt.xticks([])
plt.yticks([])

plt.subplot(1, 3, 2)

plt.imshow(conv1)
plt.xticks([])
plt.yticks([])

plt.subplot(1, 3, 3)
plt.imshow(conv2)
plt.xticks([])
plt.yticks([])

plt.show()



