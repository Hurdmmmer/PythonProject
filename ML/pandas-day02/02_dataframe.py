'''
    pandas 中的二维数组 DataFrame
'''
import pandas as pd

data = [['tom', 18], ['jerry', 19], ['jack', 22], ['rose', 22]]
# 可以设置行和列的自定义索引
df = pd.DataFrame(data=data,
                  index=['s1', 's2', 's3', 's4'],
                  columns=['name', 'age']
                  )
print(df)
print('-' *20)
# 常用的数据格式
data = {
    'name': pd.Series(['alex', 'bob', 'lena']),
    'age': pd.Series([18, 19], index=[1,2])
}
df = pd.DataFrame(data=data)
print(df)