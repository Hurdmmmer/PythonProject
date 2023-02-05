'''
    画多图
'''
import matplotlib.pyplot as plt
import numpy as np

plt.figure("subplot layout", facecolor='lightgray')

# 画分子图
for i in range(1, 10):
    plt.subplot(3, 3, i)
    plt.text(0.5, 0.5, i, size=30, ha='center', va='center')
    # 不显示x,y轴刻度
    plt.xticks([])
    plt.yticks([])


plt.show()

