'''
    数组的升维和降维操作, 视图变维
    reshape(), ravel()
    复制变维， 数据是独立的，不共享， 也会将高维度数据拉伸为一维数据
    flatten()
    就地变维，会修改当前数据。没有返回值
    resize()
'''
import numpy as np

ary = np.arange(1, 9)
# 将一维升级为二维， 并赋值给 bry， 这个操作是数据共享的， 修改数据一的数据，则数据二的数据也会改变
bry = ary.reshape(2, 4)
ary[0] = 666
print(bry)
# 降维， ravel()， 不管数据为几维数据，都会拉伸为一维数据
bry = bry.ravel()
print(bry)

cry = bry.flatten()
bry[0] = 111
print(f'bry 修改了数据{bry}')
print(f'cry 不变{cry}' )

print('就地变维')
cry.resize(2,2,2)
print(cry)

