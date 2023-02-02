'''
    读取 excel 文本，并将数据转换为需要的数组
'''
import numpy as np
import pandas as pd
import os


def load_csv(path):
    datas = []
    with open(path) as f:
        while True:
            str = f.readline().rstrip()
            if str is None or str == '':
                break
            data = str.split(',')
            datas.append(tuple(data))
    return datas


if __name__ == "__main__":
    cs_excel = load_csv(
        '/home/jeremy/PythonProject/ML/numpy-day01/test_data.csv')
    np.set_printoptions(suppress=True) 
    ary = np.array(cs_excel, dtype={
        'names': ['id', 'package_amount', 'extra_talk_time', 'extra_traffic', 'changing_behavior', 'Service_Contracts', 'Affiliate_Purchase', 'Group_Users', 'Months_of_use', 'Lost_Users'],
        'formats': ['int32', 'int32', 'float32', 'float32', 'int32', 'int32', 'int32', 'int32', 'int32', 'int32'],
    })
    print(ary)
