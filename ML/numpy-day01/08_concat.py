'''
    数组合并与拆分，水平，垂直，深度。
    深度合并，将对现有的维度进行升维
'''
import numpy as np
# 构建两个两行三列的数据，的测试数据
ary = np.arange(1, 7).reshape(2, 3)
bry = np.arange(7, 13).reshape(2, 3)
# print(ary)
# print('--------')
# # 垂直合并，水平合并
# # np.vstack() 
# # np.hstack()
# # 深度合并
# res = np.dstack((ary, bry))
# print(res)
# print(res.shape)
# # 三维数组切分的时候，不会降维，只会拆分为2个三维数组
# print('-' * 20)
# ary, bry = np.dsplit(res, 2)
# print(ary)
# print(bry)

# 若带组合的数组都是二维数组， 0 ：垂直方向，1：水平方向
# 若带组合的数组都是三维数组， 0： 垂直方向，1：水平方向，2：深度方向(必须是2个三维数组才能进行深度方向组合)
res = np.concatenate((ary, bry), axis=1)
print(res)
print('-'*20)
# 拆分中的 axis 同上。
a, b = np.split(res, 2, axis=1)
print(a)
print(b)

print('-'*20)
a = np.arange(1, 28).reshape(3, 3, 3)
b = np.arange(28, 55).reshape(3, 3, 3)
print(np.concatenate((a, b), axis=2).shape)
# 斜看页， 图像右转竖看行，图像左转竖看列
