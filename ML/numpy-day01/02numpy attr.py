'''
    ndarray 对象基本属性, 修改数组类型需要使用 astype() 方法去修改类型
    numpy 中对数据取值，使用[0,0,0] 等于使用 [0][0][0] 的方式，属于语法糖简化取值方法
'''
import numpy as np

ary = np.arange(1, 9)
print(ary.shape)
print(ary.dtype)
# 修改维度时，只要维度和数据的乘积都是原始数据的个数都可以，否则则报错
# 报错 ValueError: cannot reshape array of size 8 into shape (2,8)
# ary.shape = (2, 8)
# 下方则不会报错， 只要乘积为 8，修改维度 3，4 5 等等维度 都可以
ary.shape = (1, 8)
ary.shape = (2, 4)
ary.shape = (2, 2, 2)
print()
print(ary.shape)
print(ary)
ary.shape = (4,2,1,1)
print()
print(ary)
# 转换数据类型
res = ary.astype("float")
print(res)