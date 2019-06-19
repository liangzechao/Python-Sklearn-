# 决策树

决策树是一种树形结构的分类器，通过顺序询问分类点的属性决定分类点最终的类别。通常根据特征的信息增益或其他指标，构建一颗决策树。在分类时，只需要按照决策树中的结点依次进行判断，即可得到样本所属类别。

例如，根据下图这个构造好的分类决策树， 一个无房产，单身，年收入55K的人的会被归入 无法偿还信用卡这个类别。

![VLs5Wj.png](https://s2.ax1x.com/2019/06/18/VLs5Wj.png)

在sklearn库中，可以使用[sklearn.tree.DecisionTreeClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html) 建一个决策树用于分类，其主要参数有：

- criterion ：用于选择属性的准则，可以传入“gini”代表基尼系数，或者“entropy”代表信息增益。

- max_features ：表示在决策树结点进行分裂时，从多少个特征中选择最优特征。可以设定固定数目、百分比或其他标准。它的默认值是使用所有特征个数。


## [实例](https://github.com/liangzechao/PythonSklearnML/blob/master/2.分类/2.2决策树/DTreeClassifier.py)

也可以仿照之前 K近邻分类器的使用方法，利用 fit() 函数训练模型并使用 predict() 函数预测。

使用经验：

- 决策树本质上是寻找一种对特征空间上的划分，旨在构建一个训练数据拟合的好，并且复杂度小的决策树。

- 在实际使用中,需要根据数据情况,调整DecisionTreeClassifier类中传入的参数，比如选择合适的criterion，设置随机变量等。
