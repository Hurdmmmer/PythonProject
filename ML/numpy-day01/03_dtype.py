'''
    自定义复合类型, 只有使用元组才能转换数据类型
'''
import numpy as np
data = [
    ('zs', [100, 100, 100], 19),
    ('ww', [90, 90, 90], 19),
    ('zl', [80, 80, 80], 20)
]
# 将自定义的数据转换为 numpy 类型
# 字符串指定数据类型。
# ary = np.array(data, dtype='2str,3int32,int32')
# print(ary)
# 第二种使用类似数据库建表的方式转换数据类型
# ary = np.array(data, dtype=[('name','str',2),
#                             ('score', 'int32', 3),
#                             ('age', 'int32',1)])
# # 取值具体的列
# print(ary['name'])
# print(ary['age'])
# print(ary['score'])
# 第三种,转换数据类型
ary = np.array(data, dtype={
    'names': ['name', 'score', 'age'],
    'formats': ['2str', '3int32', 'int32'],
})

print(ary)

print(ary['name'])
print(ary['age'])
print(ary['score'])
