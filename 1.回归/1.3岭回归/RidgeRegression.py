import numpy as np
from sklearn.linear_model import Ridge              # 通过sklearn.linermodel加载岭回归方法
from sklearn import cross_validation                # 加载交叉验证模块
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures

# a=pd.read_csv('data.csv')                           # 使用pandas的方法从csv文件中加载数据
data = np.loadtxt(r'D:\Workplace\gitbook_ML\1.回归\1.3岭回归\data.csv', delimiter=",",skiprows=1)

plt.plot(data[:,5])                                 # 使用plt展示车流量信息
plt.show()

X=data[:,1:5]                                       #X用于保存0-5维数据，即属性
y=data[:,5]                                         #y用于保存第6维数据，即车流量
poly =PolynomialFeatures(6)                         #用于创建最高次数6次方的的多项式特征，多次试验后决定采用6次
X=poly.fit_transform(X)                             #X为创建的多项式特征


# 将所有数据划分为训练集和测试集，test_size表示测试集的比例，
# random_state是随机数种子
train_set_X, test_set_X, train_set_y, test_set_y = cross_validation.train_test_split(X, y, test_size=0.3, random_state=0)


# 创建回归器，并进行训练

clf =Ridge(alpha=1.0,fit_intercept=True)            # 创建岭回归实例
clf.fit(train_set_X,train_set_y)                    # 调用fit函数使用训练集训练回归器
clf.score(test_set_X,test_set_y)                    # 利用测试集计算回归曲线的拟合优度，clf.score返回值为0.7375拟合优度，


# 用于评价拟合好坏，最大为1，无最小值，
# 当对所有输入都输出同一个值时，拟合优度为0。


start =200                                          # 画一段200到300范围内的拟合曲线
end =300
y_pre =clf.predict(X)                               # 调用predict函数的拟合值
time =np.arange(start,end)

plt.plot(time,y[start:end],'b',label="real")        # 展示真实数据
plt.plot(time,y_pre[start:end],'r',label='predict') # 拟合曲线
plt.legend(loc='upper left')
plt.show()
