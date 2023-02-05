'''
    matplotlib 画图工具
'''
import numpy as np
# import matplotlib
# matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = np.array([3, 6, 9, 12, 15])

# 画直线图
plt.plot(x, y)
# plt.show()

# 绘制水平、水平的线, linestyle 线的形状， color 颜色
plt.axhline(y=5, linestyle=":", color="red")
plt.axvline(x=3, ls="-.", c="b")
# 垂直多条线段, x， 指定线条位置， ymin， ymax 指定线段起始值，终止值
plt.vlines(
    x=[1,2,4],
    ymin=[1, 3, 10],
    ymax=[6, 10, 15]
)


plt.show()
