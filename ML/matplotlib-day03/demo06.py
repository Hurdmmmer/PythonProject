'''
    自定义布局
'''
import matplotlib.pyplot as plt

plt.figure('flow layout', facecolor='lightgray')


plt.axes([0.03, 0.03, 0.5, 0.9])
plt.text(0.5, 0.5, 'hello', ha='center', va='center', size=30)
plt.grid()

plt.show()