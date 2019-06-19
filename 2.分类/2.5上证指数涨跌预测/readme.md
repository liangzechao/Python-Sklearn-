# 上证指数涨跌预测

## 1.数据介绍：

网易财经上获得的上证指数的历史数据，爬取了20年的上证指数数据。

## 2.实验目的： 

根据给出当前时间前150天的历史数据，预测当天上证指数的涨跌。

## [3.数据实例](https://github.com/liangzechao/PythonSklearnML/blob/master/2.分类/2.5上证指数涨跌预测/stock)
中核科技1997年到2017年的股票数据部分截图，红框部分为选取的特征值数据实例

![VXKbXn.md.png](https://s2.ax1x.com/2019/06/19/VXKbXn.png)

## [4.实验过程](https://github.com/liangzechao/PythonSklearnML/blob/master/2.分类/2.5上证指数涨跌预测/IndexForecast.py)

[sklearn.svm.SVC](https://scikit-learn.org/stable/modules/generated/sklearn.svm.SVC.html)

![VXl3Y8.png](https://s2.ax1x.com/2019/06/19/VXl3Y8.png)

## [5.实验结果](https://github.com/liangzechao/PythonSklearnML/blob/master/2.分类/2.5上证指数涨跌预测/result.txt)

如运用两个核函数做实验，准确率由表中数据所示。5次交叉验证的准确率相近，均为53%左右。

![VXlCe1.md.png](https://s2.ax1x.com/2019/06/19/VXlCe1.md.png)

## 6.交叉验证：

交叉验证法先将数据集D划分为k个大小相似的互斥子集，每个自己都尽可能保持数据分布的一致性，即从D中通过分层采样得到。然后，每次用k-1个子集的并集作为 训练集，余下的那个子集作为测试集；这样就可获得k组训练/测试集，从而可进行k 次训练和测试，最终返回的是这个k个测试结果的均值。通常把交叉验证法称为“k者 交叉验证”, k最常用的取值是10，此时称为10折交叉验证。

![](https://s2.ax1x.com/2019/06/19/VXlDYT.png)
