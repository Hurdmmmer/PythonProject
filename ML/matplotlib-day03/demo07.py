'''
    散点图, 查看数据分布情况
'''
import matplotlib.pyplot as plt
import numpy as np


# 参数一：期望值，参数二：标准差， 参数三：生成数量
# nomal 这个函数生成的正态分布的数据为，三倍标准差的概率为 97%左右， 67% 在一倍的标准差中
data1 = np.random.normal(100, 10, 500)

# 标准差越小， 生成的随机数震荡幅度越小
data2 = np.random.normal(100, 10, 500)

# 绘制散点图
plt.scatter(x=data1, y=data2, marker='o', s=10, color='blue')
# plt.scatter(x=data2, y=data2, marker='o', s=10, color='red')

# 设置轴刻度范围
plt.xlim(0, 150)
plt.ylim(0, 159)
# 设置刻度
plt.xticks(range(0, 151, 10))
plt.yticks(range(0, 151, 10))


# 现在轴标签
plt.xlabel('x')
plt.ylabel('y')

# 设置 x y 轴对齐0点
ax = plt.gca()
ax_left = ax.spines['left']
ax_left.set_position(("data", 100))

ax_buttom = ax.spines['bottom']
ax_buttom.set_position(("data", 100))

# 去掉指定位置的边框
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)


plt.show()

