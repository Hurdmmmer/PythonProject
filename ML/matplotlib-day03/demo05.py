'''
    网格化布局
'''
import matplotlib.pyplot as plt
import matplotlib.gridspec as mg

plt.figure("grid layout", facecolor='lightgray')
# 创建3 x 3 的网格对象
gs = mg.GridSpec(3, 3)
# 选择指定1号画布和2号画布网格中的画布,并合并
plt.subplot(gs[0:3])
#在选择的画布中写入文本
plt.text(0.5, 0.5, "test", size=20, ha='center', va='center')
# 画出网格线
plt.grid(linestyle=':', color='red')
# 紧凑布局
plt.tight_layout()

plt.subplot(gs[6])
plt.text(0.5, 0.5, "scene", size=20, ha='center', va='center')

plt.show()