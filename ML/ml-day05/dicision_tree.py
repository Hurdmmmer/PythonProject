'''
    决策树, 使用决策树预测波士顿房价
'''
import sklearn.datasets as sd
import sklearn.tree as st
import sklearn.model_selection as ms
import sklearn.metrics as sm
import warnings
warnings.filterwarnings("ignore")

data = sd.load_boston()
# 整理输入输出
x = data.data
y = data.target

# 该方法用于划分测试集和训练集，test_size 表示测试集在整个样本数据中的占比
# 自动划分数据， 该方法是一个随机划分, random_state 指定随机种子，每次去的值都是一样的。正常环境下不会使用
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.2, random_state=7)
# criterion = mse 表示使用了均方误差来作为最优划分策略
model = st.DecisionTreeRegressor(criterion='mse', max_depth=6)


model.fit(train_x, train_y)

pre_train_y = model.predict(train_x)
pre_test_y = model.predict(test_x)

print(f'决策树回归 R2 得分 {sm.r2_score(train_y, pre_train_y)}')
print(f'决策树回归 R2 得分 {sm.r2_score(test_y, pre_test_y)}')