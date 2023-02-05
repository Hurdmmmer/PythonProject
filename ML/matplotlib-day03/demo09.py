'''
    柱状图
'''
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


plt.figure('柱状图', dpi=200, facecolor='lightgray')

apples = np.array([30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])
x = np.arange(1, 13)

plt.xlabel('月份', fontsize=14)
plt.ylabel('价格', fontsize=14)

plt.tick_params(labelsize=10)
plt.grid(axis='y', linestyle=':')
plt.ylim((0, 40))

plt.bar(x-0.2, apples, 0.4, color='pink', alpha=0.8, label='苹果')
plt.bar(x + 0.2, oranges, 0.4, color='orange', alpha=0.8, label='橙子')


plt.xticks(range(1,13))

plt.legend()
plt.show()
