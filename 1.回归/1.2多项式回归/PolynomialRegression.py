import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures            #导入线性模型和多项式特征构造模块


# 读取数据集
datasets_X = []
datasets_Y = []
fr = open('prices.txt','r')                     # 一次读取整个文件
lines = fr.readlines()
for line in lines:                              # 逐行进行操作，循环遍历所有数据
    items = line.strip().split(',')
    datasets_X.append(int(items[0]))            #将读取的数据转换为int型，并分别写入datasets_X和datasets_Y
    datasets_Y.append(int(items[1]))

length = len(datasets_X)
datasets_X = np.array(datasets_X).reshape([length,1])
datasets_Y = np.array(datasets_Y)

minX = min(datasets_X)
maxX = max(datasets_X)
X = np.arange(minX,maxX).reshape([-1,1])

# degree=2 表示建立datasets_X的二次多项式特征X_poly
poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(datasets_X)
lin_reg_2 = linear_model.LinearRegression()
lin_reg_2.fit(X_poly, datasets_Y)

print(poly_reg)
#查看回归方程系数
print('Cofficients:',lin_reg_2.coef_)
#查看回归方程截距
print('intercept',lin_reg_2.intercept_)

# 图像中显示
plt.scatter(datasets_X, datasets_Y, color = 'red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color = 'blue')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()