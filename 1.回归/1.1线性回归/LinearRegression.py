import matplotlib.pyplot as plt                 #表示matplotlib的pyplot子库，它提供了和matlab类似的绘图API
import numpy as np
from sklearn import linear_model                #表示可以调用sklearn中的 linear_model模块进行线性回归。

# 读取数据集  
# 建立datasets_X和datasets_Y用来存储数据中的房屋尺寸和房屋成交价格。
datasets_X = []
datasets_Y = []
fr = open('prices.txt','r')                     # 一次读取整个文件。
lines = fr.readlines()
for line in lines:                              # 逐行进行操作，循环遍历所有数据
    items = line.strip().split(',')
    datasets_X.append(int(items[0]))            # 将读取的数据转换为int型，并分别写入datasets_X和datasets_Y。
    datasets_Y.append(int(items[1]))

length = len(datasets_X)                                    # 求得datasets_X的长度，即为数据的总数。
datasets_X = np.array(datasets_X).reshape([length,1])       # 将datasets_X转化为数组， 并变为二维，以符合线性回 归拟合函数输入参数要求
datasets_Y = np.array(datasets_Y)                           # 将datasets_Y转化为数组

#以数据datasets_X的最大值和最小值为范围，建立等差数列，方便后续画图。
minX = min(datasets_X)
maxX = max(datasets_X)
X = np.arange(minX, maxX).reshape([-1,1])

# 调用线性回归模块，建立回归方程，拟合数据
linear = linear_model.LinearRegression()
linear.fit(datasets_X, datasets_Y)

# 查看回归方程系数
print('Cofficients:',linear.coef_)
# 查看回归方程截距
print('intercept',linear.intercept_)

# 可视化处理，图像中显示
plt.scatter(datasets_X, datasets_Y, color = 'red')      # scatter函数用于绘制数据 点，这里表示用红色绘制数据点；
plt.plot(X, linear.predict(X), color = 'blue')          # plot函数用来绘制直线，这里表示用蓝色绘制回归线；
plt.xlabel('Area')                                      # xlabel和ylabel用来指定横纵坐标的名称
plt.ylabel('Price')
plt.show()