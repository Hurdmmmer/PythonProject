'''
    常用的统计指标
'''
import pandas as pd
import numpy as np
data = pd.read_json('/home/jeremy/PythonProject/ML/data_test/ratings.json')
print(data)
# 取出行数据需要使用 .loc 来进行选择，否则报错
faracture = data.loc['Fracture']


# 均值
print(np.mean(faracture))
# pandas 二维数组中求均值，需要使用  axis 来指定均值的方向(0-垂直，1-水平)
print(data.mean(axis=1))

# 使用权重均值
weights = [1, 10, 1, 1, 1, 10, 1]
print(np.average(faracture, weights=weights))
# 获取最大值索引
print(np.argmax(faracture))
# pandas 中返回的是标签索引
print(faracture.idxmax())

# 标准差
# 多维数组, axis 计算的方向
print(data.std(axis=0))
print(data.std(axis=1))
# 一维数组， pandas 中默认为样本方差
print(faracture.std())
# numpy 中的方差是总体方差， ddof 设置计算方差公式中 n-1的部分
print(np.std(faracture, ddof=1))