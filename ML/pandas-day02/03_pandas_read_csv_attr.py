'''
    pandas 中读取文本文件常用的参数
    方法参数
    filepath_or_buffer  文件路径
    sep                 列之间的分隔符。read_csv()默认为‘,’ read_table() 默认为/t
    header              默认将首行设为列名。header=None时应手动给出列名。
    names               header=None时设置此字段使用列表初始化列名
    index_col           将某一列作为行级索引。若使用列表，则设置复合索引。
    usecols             选择读取文件中的某些列。设置为为相应列的索引列表。
    skiprows            跳过行。可选择跳过前n行或给出跳过的行索引列表。
    encoding            编码。
'''
import pandas as pd

data = pd.read_csv('/home/jeremy/PythonProject/ML/numpy-day01/test_data.csv', header=None,
                   # 设置列名
                   names=['index', 'package_amount', 'extra_talk_time', 'extra_traffic', 'changing_behavior',
                          'Service_Contracts', 'Affiliate_Purchase', 'Group_Users', 'Months_of_use', 'Lost_Users'],
                   # 将数据中的一列设置为行级索引列， 不让数据自动生成新的默认索引列
                   index_col='index'
                   )
print(data)