'''
    ndarray 创建
'''
import numpy as np
# 构建一个一维数组， np 创建的数组做数学运算时（加减乘除）会建数组中的每一个元素都取出来进行运算
# 数组与数组间运算，如果数组长度不一致则报错
ary = np.array([1, 2, 3, 4, 5, 6])

print(ary * 2)
print(ary == 3)

print(type(ary))
# numpy 中的 arang 方法, np 中的 步长可以设置为浮点数
ary = np.arange(1, 10, 2)
print(ary)
ary = np.arange(1, 2, 0.1)
print(ary)
# 构建初始值为 0 的长度为10的数组, dtype 设置数组的类型
ary = np.zeros(shape=(2, 2), dtype='int64')
print(ary)
# 获取相同维度的数组，并以 0 填充
res = np.zeros_like(ary)
print(res)
