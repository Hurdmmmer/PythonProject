'''
    在 pandas 中
    Series  是一个带索引的一维数组
    DataFrame 是带索引的二维数组
'''
import pandas as pd
import numpy as py

data = [10, 11, 12, 13, 14]
# 使用 index 自定义每一个数据的索引
s = pd.Series(data=data, index=['zs', 'ls', 'ww', 'zl', 'tq'])
# 获取数据的方式
print(s[0])
print(s[0:2])
# 掩码操作
print(s[[0, 1, 3]])
# 使用自定义索引切片时，时包含最后一个数据的
print(s['zs'])
print(s['zs':'ww'])
# 掩码操作
print(s[['zs','ww']])


#还可以使用字典构建数据
data = {
    '101':'zs',
    '102':'ls'
}
s = pd.Series(data=data)
print(s)
print('--------')
# 使用标量（常量）直接构建一个一维数组
s = pd.Series(0.2, index=range(10))
print(s)