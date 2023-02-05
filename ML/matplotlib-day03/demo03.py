'''
    绘制二次函数图像， 二次函数（quadratic function）的基本表示形式为y=ax²+bx+c（a≠0）。
    二次函数最高次必须为二次， 二次函数的图像是一条对称轴与y轴平行或重合于y轴的抛物线。
    二次函数方程：y=ax²+bx+c（a≠0） 【a, b, c】 为常数 a为负数，开口朝下
'''
import numpy as np
import matplotlib.pyplot as plt
# 设置窗口名称, 设置窗口大小，设置分辨率
plt.figure("test_01", figsize=(5, 3), dpi=300)

x = np.arange(-5, 5, step=0.01)
# 使用方程计算 y 的每一个坐标
y = (x**2) + 1

plt.plot(x, y, linestyle=":", color="red", linewidth=2, label='$y =x^2$')

# 绘制特殊点
x_tck = np.array([-2, 1, 4])
y_tck = x_tck ** 2 + 1
# marker 设置点的形状, 具体参数请百度
plt.scatter(x=x_tck, y=y_tck, marker='o', s=60, color='blue')


plt.annotate(
    'point',
    xycoords="data",
    # 标注哪一个点
    xy=(4, 17),
    textcoords="offset points",
    # 备注坐标，
    xytext=(40, 30),
    fontsize=14,
    # 连接线
    arrowprops=dict(
            arrowstyle='->',
            connectionstyle='arc3'
    ),
)

plt.title("quadratic function")
plt.xlabel('x')
plt.ylabel('y')

# 设置刻度范围
plt.xlim(-7, 7)
plt.ylim(-0, 30)

# 设置刻度序列
plt.xticks(np.arange(-7, 8, 2))
plt.yticks(range(-0, 30, 4))
# 设置坐标轴位置 left 设置 y 轴的左右位置。 buttom 设置x轴的上下位置
ax = plt.gca()
ax_left = ax.spines['left']
ax_left.set_position(("data", 0))

ax_buttom = ax.spines['bottom']
ax_buttom.set_position(("data", 0))
# 去掉指定位置的边框
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.legend()
plt.show()
