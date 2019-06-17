## 1.基本概念

线性回归(Linear Regression)是利用数理统计中回归分析， 来确定两种或两种以上变量间相互依赖的定量关系的一种统计分 析方法。 

线性回归利用称为线性回归方程的最小平方函数对一个或多个自变量和因变量之间关系进行建模。这种函数是一个或多个称为回 归系数的模型参数的线性组合。只有一个自变量的情况称为简单 回归,大于一个自变量情况的叫做多元回归。

[![VbmLlV.md.png](https://s2.ax1x.com/2019/06/17/VbmLlV.md.png)](https://imgchr.com/i/VbmLlV)
## 2.用途

线性回归有很多实际的用途，分为以下两类： 

1.如果目标是预测或者映射，线性回归可以用来对观测数据集的y和X的值拟合出一个预测模型。当完成这样一个模型以后，对于一个新增的X值， 在没有给定与它相配对的y的情况下，可以用这个拟合过的模型预测出一个 y值。

2.给定一个变量y和一些变量X1,⋯,Xp,这些变量有可能与y相关，线 性回归分析可以用来量化y与Xj之间相关性的强度，评估出与y不相关的Xj， 并识别出哪些Xj的子集包含了关于y的冗余信息。

## 3.实例

与房价密切相关的除了单位的房价，还有房屋的尺寸。我们可以根 据已知的房屋成交价和房屋的尺寸进行线性回归，继而可以对已知房屋尺 寸，而未知房屋成交价格的实例进行成交价格的预测。

目标：对房屋成交信息建立回归方程，并依据回归方程对房屋价格进行预测 

## 4.数据

为了方便展示，成交信息只使用了房屋的面积以及对应的成交价格。 其中： 

- 房屋面积单位为平方英尺（ft2）
- 房屋成交价格单位为万

[数据在这](https://github.com/liangzechao/PythonSklearnML/blob/master/1.回归/1.1线性回归/prices.txt)

![VbnBcV.png](https://s2.ax1x.com/2019/06/17/VbnBcV.png)

##  5.可行性分析

- 简单而直观的方式是通过数据的可视化直接观察房屋成交价格与房 屋尺寸间是否存在线性关系。

- 对于本实验的数据来说，散点图就可以很好的将其在二维平面中进 行可视化表示。

## 6.实验过程

使用算法：线性回归 

实现步骤： 1.建立工程并导入sklearn包 

                  2.加载训练数据，建立回归方程

                  3.可视化处理

调用[sklearn.linear_model.LinearRegression()](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html)所需参数：

- fit_intercept : 布尔型参数，表示是否计算该模型截距。可选参数。

- normalize : 布尔型参数，若为True，则X在回归前进行归一化。可选参数。默认值为False。

- copy_X : 布尔型参数，若为True，则X将被复制；否则将被覆盖。可选参数。默认值为True。

- n_jobs : 整型参数，表示用于计算的作业数量；若为-1，则用所有的CPU。可选参数。默认值为1。

线性回归fit函数用于拟合输入输出数据，调用形式为[linear.fit(X,y, sample_weight=None)](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html#sklearn.linear_model.LinearRegression.fit):

- X : X为训练向量；

- y : y为相对于X的目标向量； 

- sample_weight : 分配给各个样本的权重数组，一般不需要使用，可省略。

## [7.代码](https://github.com/liangzechao/PythonSklearnML/blob/master/1.回归/1.1线性回归/LinearRegression.py)

## 8.运行结果
![VbK5wD.png](https://s2.ax1x.com/2019/06/17/VbK5wD.png)