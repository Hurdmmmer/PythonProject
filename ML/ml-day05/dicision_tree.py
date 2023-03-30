'''
    决策树, 使用决策树预测波士顿房价
'''
import sklearn.datasets as sd
import sklearn.tree as st
import sklearn.model_selection as ms
import sklearn.metrics as sm
import pandas as pd
import numpy as np
import sklearn.ensemble as se  # 权重树，学习模块组合决策树树的
import matplotlib.pyplot as plt


def adaboostDicisonTree():
    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]

    # 整理输入输出
    x = data
    y = target

    # 该方法用于划分测试集和训练集，test_size 表示测试集在整个样本数据中的占比
    # 自动划分数据， 该方法是一个随机划分, random_state 指定随机种子，每次去的值都是一样的。正常环境下不会使用
    train_x, test_x, train_y, test_y = ms.train_test_split(
        x, y, test_size=0.2, random_state=7)
    # criterion = squared_error 表示使用了均方误差来作为最优划分策略
    model = st.DecisionTreeRegressor(criterion='squared_error', max_depth=4)
    # 使用 Adaboost 构建正向激励决策树复合模型
    # n_estimators 构建指定数量的决策树（弱模型-基础模型）
    # random_state 随机权重的种子
    model = se.AdaBoostRegressor(model, n_estimators=400, random_state=7)

    model.fit(train_x, train_y)

    # 将数据特征的权重画出来。
    fi = model.feature_importances_
    series = pd.Series(fi, index=[
       'CRIM',
       'ZN',
       'INDUS',
       'CHAS',
       'NOX',
       'RM',
       'AGE',
       'DIS',
       'RAD',
       'TAX',
       'PTRATIO',
       'B',
       'LSTAT',
       ])
    
    series = series.sort_values(ascending=True)
    
    # 绘制柱状图
    plt.bar(series.index, series.values)
    plt.title('Bar Chart')
        # 旋转 x 轴标签
    plt.xticks(rotation=45)
    # 保存图像
    plt.savefig('./ml-day05/bar_chart.png')


    pre_train_y = model.predict(train_x)
    pre_test_y = model.predict(test_x)

    print(f'决策树回归 R2 得分 {sm.r2_score(train_y, pre_train_y)}')
    print(f'决策树回归 R2 得分 {sm.r2_score(test_y, pre_test_y)}')



def gpdtDicisonTree():
    '''GPDT 决策树模型'''

    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]

    # 整理输入输出
    x = data
    y = target

    # 该方法用于划分测试集和训练集，test_size 表示测试集在整个样本数据中的占比
    # 自动划分数据， 该方法是一个随机划分, random_state 指定随机种子，每次去的值都是一样的。正常环境下不会使用
    train_x, test_x, train_y, test_y = ms.train_test_split(
        x, y, test_size=0.2, random_state=7)
    # max_depth 最大递归深度
    # n_estimators 弱模型数量
    # min_samples_split 最小分割节点数量
    model = se.GradientBoostingRegressor(max_depth=4, n_estimators=400, min_samples_split=2)

    model.fit(train_x, train_y)
    
    pre_train_y = model.predict(train_x)
    pre_test_y = model.predict(test_x)

    print(f'GPDT 决策树回归 R2 得分 {sm.r2_score(train_y, pre_train_y)}')
    print(f'GPDT 决策树回归 R2 得分 {sm.r2_score(test_y, pre_test_y)}')

def randomDicisonTree():
    '''随机森林 决策树模型'''

    data_url = "http://lib.stat.cmu.edu/datasets/boston"
    raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)

    data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
    target = raw_df.values[1::2, 2]

    # 整理输入输出
    x = data
    y = target

    # 该方法用于划分测试集和训练集，test_size 表示测试集在整个样本数据中的占比
    # 自动划分数据， 该方法是一个随机划分, random_state 指定随机种子，每次去的值都是一样的。正常环境下不会使用
    train_x, test_x, train_y, test_y = ms.train_test_split(
        x, y, test_size=0.2, random_state=7)
 
    # max_depth 最大递归深度
    # n_estimators 弱模型数量
    # min_samples_split 最小分割节点数量
    model = se.RandomForestRegressor(max_depth=4, n_estimators=400, min_samples_split=2)

    model.fit(train_x, train_y)
    
    pre_train_y = model.predict(train_x)
    pre_test_y = model.predict(test_x)

    print(f'随机森林回归 R2 得分 {sm.r2_score(train_y, pre_train_y)}')
    print(f'随机森林回归 R2 得分 {sm.r2_score(test_y, pre_test_y)}')

if __name__ == "__main__":
    gpdtDicisonTree()
    randomDicisonTree()
