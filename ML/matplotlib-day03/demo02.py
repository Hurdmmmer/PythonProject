'''
    绘制正弦，余弦，曲线
'''
import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(0, 2*np.pi, 0.1)
# 使用  sin cos 函数计算每一个点的正弦和余弦
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='sin')
plt.plot(x, y2, linestyle=":", linewidth=4, color="red", label='cos')


plt.title("cos & sin")
plt.xlabel('x')
plt.ylabel('y')

# 设置 x y轴的刻度
plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

# 指定轴上面的刻度, 第一个参数设置刻度， 第二个参数设置每个刻度的名称，不支持中文
# plt.xticks([1,3,5,7], ['d', 'a', 'b', 'c'])
plt.xticks([1,3,5,7])
plt.yticks([-1, 0, 1])
# loc 指定图例显示的位置
plt.legend(loc=0) # 显示图例
plt.show()
