'''
    二项分布是重复 n 次独立实验，每次实验的结果只有2中可能。且结果是互相对立的。概率保持不变
    二项分布，可以用于求特地场景下概率的近似值。
    1. 某人投篮命中率 0.3。投 10 次 投进 5 球的概率
'''
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 某人打客服电话，客服接通率 0.6， 一共打了3次，都没人接的概率为多少
# 参数一：实验次数，参数二：实验期望概率，参数三：实验几次， 结果为：随机生成符合期望概率的需要执行实验的次数
result = np.random.binomial(10, 0.6, 1000)
# 统计结果为0的概率（结果为0，则表示没人接）
res = result == 0
# print(result)
# 统计为拒接的数量除以实验次数即可计算出模拟拒接的概率
print(res.sum() / 1000)

# 绘制直方图
# x 为要绘制的数据，一维数组可用pandas的Series结构，二维数组使用DataFrame
# bins 指定条带bar 的总个数，个数越多，条形带越紧密。
# range :筛选数据范围，默认是最小到最大的取值范围
plt.hist(
    x = result,
    bins=11,
    label='二项分布'
)

plt.legend()
plt.show()