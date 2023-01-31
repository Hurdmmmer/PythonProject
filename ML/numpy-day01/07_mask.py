'''
    数组的掩码操作
'''
import numpy as np

ary = np.arange(1, 101)
# 求出 100 内 3 的倍数
# 使用的原理为， 数组数学运算时， 会将数组中的每一个元素都会取出来进行计算。
# ary % 3 的数学运算的结果为 [1 2 0 1 2 0 1 2 ...]
# ary % 3 == 0 会将上面的结果转换为布尔值。 [False False ...]
print(ary % 3 == 0)
print('---------')
# 这里的操作将会时使用了 ary[[false false true ...]]， 这个结果将会是取出数组中满足 true 的值
res = ary[ary % 3 == 0]
print(res)