'''
    预测骑车
'''
import pandas as pd
import sklearn.tree as st
import sklearn.model_selection as ms
import sklearn.metrics as sm
import sklearn.ensemble as se

import numpy as np


raw_df = pd.read_csv('./data_test/bike_day.csv', skiprows=1, header=None)
del raw_df[1]
del raw_df[0]
del raw_df[13]
del raw_df[14]
# 准备数据, 使用切片的功能获取 第一个是表示所有行都要， 第二个表示 不要最后一列(第一列开始到最后一列数据。不包含最后一列) -1 表示最后一列
x = raw_df.iloc[:, :-1]
# 这里的切片表示， 要所有的行， 只要最后一列, 使用 -1 表示从最后一行。
# -2 表示只要倒数第二列。 '-2：' 表示从最后第二列开始都要
y = raw_df.iloc[:, -1:]


train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.2, random_state=7)

# 构建决策树模型
# min_samples_split 指定每一个节点中最小的样本数量
model = st.DecisionTreeRegressor(max_depth=10, min_samples_split=4)
# 构建 adaboost 回归决策树
model = se.AdaBoostRegressor(model, n_estimators=1000, random_state=7)

model.fit(train_x, train_y.values.ravel())

print(f'模型的权重是：{model.feature_importances_}')

pre_train_y = model.predict(train_x)
pre_test_y = model.predict(test_x)


print(f'训练集r2得分： {sm.r2_score(train_y, pre_train_y)}')
print(f'测试集r2得分： {sm.r2_score(test_y, pre_test_y)}')

print(sm.mean_absolute_error(test_y, pre_test_y))