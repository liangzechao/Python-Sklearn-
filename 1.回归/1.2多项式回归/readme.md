## 1.基本概念

多项式回归(Polynomial Regression)是研究一个因变量与一个或多个自变量间多项式的回归分析方法。如果自变量只有一个 时，称为一元多项式回归；如果自变量有多个时，称为多元多项式回归。 

[![VbM01I.md.png](https://s2.ax1x.com/2019/06/17/VbM01I.md.png)](https://imgchr.com/i/VbM01I)
        

1.在一元回归分析中，如果依变量y与自变量x的关系为非线性的，但是又找不到适当的函数曲线来拟合，则可以采用一元多项式回归。 

2.多项式回归的最大优点就是可以通过增加x的高次项对实测点进行逼近，直至满意为止。 

3.事实上，多项式回归可以处理相当一类非线性问题，它在回归分析 中占有重要的地位，因为任一函数都可以分段用多项式来逼近。

[![VbMgAg.md.png](https://s2.ax1x.com/2019/06/17/VbMgAg.md.png)](https://imgchr.com/i/VbMgAg)


## 2.实例

我们在前面已经根据已知的房屋成交价和房屋的尺寸进行了线 性回归，继而可以对已知房屋尺寸，而未知房屋成交价格的实例进行了成 交价格的预测，但是在实际的应用中这样的拟合往往不够好，因此我们在 此对该数据集进行多项式回归。

目标：对房屋成交信息建立多项式回归方程，并依据回归方程对房屋价格进行预测 

[![VbM2NQ.md.png](https://s2.ax1x.com/2019/06/17/VbM2NQ.md.png)](https://imgchr.com/i/VbM2NQ)

## [3.数据](https://github.com/liangzechao/PythonSklearnML/blob/master/1.回归/1.2多项式回归/prices.txt)

## [4.代码](https://github.com/liangzechao/PythonSklearnML/blob/master/1.回归/1.2多项式回归/PolynomialRegression.py)




## 5.结果
通过多项式回归拟合的曲线与 数据点的关系如下图所示。依据该 多项式回归方程即可通过房屋的尺 寸，来预测房屋的成交价格。
![VbQPED.png](https://s2.ax1x.com/2019/06/17/VbQPED.png)