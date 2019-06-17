## 1.基本概念

岭回归是在结构风险最小化的正则化因子上使用模型参数向量的二范数形式。那么，如果使用一范数形式，那就是lasso回归了。

[![Vb8pzd.md.png](https://s2.ax1x.com/2019/06/17/Vb8pzd.md.png)](https://imgchr.com/i/Vb8pzd)

![Vb8iLt.gif](https://s2.ax1x.com/2019/06/17/Vb8iLt.gif)

岭回归与Lasso回归最大的区别在于岭回归引入的是L2范数惩罚项，Lasso回归引入的是L1范数惩罚项，Lasso回归能够使得损失函数中的许多θ均变成0，这点要优于岭回归，因为岭回归是要所有的θ均存在的，这样计算量Lasso回归将远远小于岭回归。

## 2.实例

数据介绍： 数据为某路口的交通流量监测数据，记录全年小时级别的车流量。 

实验目的： 根据已有的数据创建多项式特征，使用岭回归模型代替一般的线性模型，对车流量的信息进行多项式回归。

## [3.数据](https://github.com/liangzechao/PythonSklearnML/blob/master/1.回归/1.4lasso回归/data.csv)

## [4.代码](https://github.com/liangzechao/PythonSklearnML/blob/master/1.回归/1.4lasso回归/LassoRegression.py)

