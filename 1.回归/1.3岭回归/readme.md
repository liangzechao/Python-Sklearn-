## 1.基本概念

对于一般地线性回归问题，参数的求解采用的是最小二乘法，其目标函数如下：
[![VbQG2n.md.png](https://s2.ax1x.com/2019/06/17/VbQG2n.md.png)](https://imgchr.com/i/VbQG2n)


参数w的求解，也可以使用如下矩阵方法进行： 
[![VbQJvq.md.png](https://s2.ax1x.com/2019/06/17/VbQJvq.md.png)](https://imgchr.com/i/VbQJvq)
      

对于矩阵X，若某些列线性相关性较大（即训练样本中某些属性线性相关），就会导致，就会导致XTX的值接近0，在计算(XTX)-1时就会出现不稳定性： 

**结论：传统的基于最小二乘的线性回归法缺乏稳定性。**

[![VbQHMt.md.png](https://s2.ax1x.com/2019/06/17/VbQHMt.md.png)](https://imgchr.com/i/VbQHMt)



**岭回归(ridge regression)是一种专用于共线性数据分析的有偏估计回归方法,是一种改良的最小二乘估计法，对某些数据的拟合要强于最小二乘法。**

在sklearn库中，可以使用[sklearn.linear_model.Ridge](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Ridge.html)调用岭回归模型，其主要参数有：

- alpha：正则化因子，对应于损失函数中的α
- fit_intercept：表示是否计算截距，
- solver：设置计算参数的方法，可选参数‘auto’、‘svd’、‘sag’等

## 2.实例

数据介绍： 数据为某路口的交通流量监测数据，记录全年小时级别的车流量。 

实验目的： 根据已有的数据创建多项式特征，使用岭回归模型代替一般的线性模型，对车流量的信息进行多项式回归。

## [3.数据](https://github.com/liangzechao/PythonSklearnML/blob/master/1.回归/1.3岭回归/data.csv)

## 4.代码

