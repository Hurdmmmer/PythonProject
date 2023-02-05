'''
    填充图像
'''
import matplotlib.pyplot as plt
import numpy as np
import math

ary = np.arange(0, 8*np.pi, 0.1)

sin = np.sin(ary)
cos = np.cos(ary / 2) / 2

plt.plot(ary, sin, linestyle=':', label="$y=sin(x)$", color='red')
plt.plot(ary, cos, label="$y=cos(x)$")


# 填充颜色
plt.fill_between(ary, sin, cos, sin > cos, color='green')
plt.fill_between(ary, sin, cos, sin < cos, color='pink')


plt.ylim(-1.5, 2)
plt.xticks(range(0, 25, 2))


plt.grid()

plt.legend()
plt.show()
