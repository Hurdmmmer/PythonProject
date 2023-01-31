'''
    测试 numpy 时间日期类型
'''
import numpy as np
date = np.array(['2011', '2012-01-01', '2013-01-01 08:08:08'])
print(date)
# 转换为时间日期类型, 指定转换日期的类型 年 月 日
# date = date.astype('datetime64[D]')
# date = date.astype('datetime64[s]')
# date = date.astype('datetime64[M]')
date = date.astype(np.datetime64)
print(date, date.dtype)
# 时间戳转换为 int64 类型
date = date.astype(np.int64)
print(date, date.dtype)
