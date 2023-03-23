'''
    波士顿房价预测
'''
import sklearn.datasets as sd
import sklearn.model_selection as ms  # 模型选择模块
import sklearn.linear_model as lm
import sklearn.metrics as sm
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import warnings

warnings.filterwarnings("ignore")

data = sd.load_boston()

# 整理输入输出
x = data.data
y = data.target

# 该方法用于划分测试集和训练集，test_size 表示测试集在整个样本数据中的占比
# 自动划分数据， 该方法是一个随机划分, random_state 指定随机种子，每次去的值都是一样的。正常环境下不会使用
train_x, test_x, train_y, test_y = ms.train_test_split(x, y, test_size=0.2, random_state=7)

# 使用线性模型
model = lm.LinearRegression()
model.fit(train_x, train_y)
# 预测
pred_test_y = model.predict(test_x)
pred_train_y = model.predict(train_x)

# 对模型进行 R2 评分, 当R2得分都不高时，表示欠拟合
print(f'训练集R2 {sm.r2_score(train_y, pred_train_y)}')
print(f'测试集R2 {sm.r2_score(test_y, pred_test_y)}')
print("=" * 40)
# 使用岭回归对样本数据进行拟合
model = lm.Ridge(alpha=1)
model.fit(train_x, train_y)
# 预测
pred_test_y = model.predict(test_x)
pred_train_y = model.predict(train_x)

# 对模型进行 R2 评分, 当R2得分都不高时，表示欠拟合
print(f'岭回归训练集R2 {sm.r2_score(train_y, pred_train_y)}')
print(f'岭回归测试集R2 {sm.r2_score(test_y, pred_test_y)}')
print("=" * 40)

# 使用多项式对模型的复杂度进行提升。上面使用的发现模型精度不够。需要提升模型的复杂度
# 使用多项式中 PolynomialFeatures 指定次幂，就是提高模型的精度。越大需要的内存越大，精度越高
# 需要注意的是，次幂越高，会导致模型过拟合。这里需要配置合适的值
model = pl.make_pipeline(sp.PolynomialFeatures(2), lm.LinearRegression())
model.fit(train_x, train_y)
# 预测
pred_test_y = model.predict(test_x)
pred_train_y = model.predict(train_x)

# 对模型进行 R2 评分, 当R2得分都不高时，表示欠拟合
print(f'多项式回归训练集R2 {sm.r2_score(train_y, pred_train_y)}')
print(f'多项式回归测试集R2 {sm.r2_score(test_y, pred_test_y)}')
