# K近邻分类器（KNN）

KNN：通过计算待分类数据点，与 已有数据集中的所有数据点的距离。取 距离最小的前K个点，根据“少数服从 多数“的原则，将这个数据点划分为出 现次数最多的那个类别。

如下图xu点，应分类为w1类别。

![VLsuZT.png](https://s2.ax1x.com/2019/06/18/VLsuZT.png)

在sklearn库中，可以使用[sklearn.neighbors.KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) 创建一个K近邻分类器，主要参数有：

- n_neighbors：用于指定分类器中K的大小(默认值为5，注意与 kmeans的区别) 
- weights：设置选中的K个点对分类结果影响的权重（默认值为平均 权重"uniform"，可以选择“distance”代表越近的点权重越高， 或者传入自己编写的以距离为参数的权重计算函数）

它的主要参数还有：

- algorithm：设置用于计算临近点的方法，因为当数据量很大的情况 下计算当前点和所有点的距离再选出最近的k各点，这个计算量是很费时的，所以（选项中有ball_tree、kd_tree和brute，分别代表不同的寻找邻居的优化算法，默认值为auto，根据训练数据自动选择）

## [实例](https://github.com/liangzechao/PythonSklearnML/blob/master/2.分类/2.1KNN/KNNClassifier.py)


使用经验：

在实际使用时，我们可以使用所有训练数据构成特征 X 和标签 y，使用 fit() 函数进行训练。在正式分类时，通过一次性构造测试集或者一个一个输入样本的方式，得到样本对应的分类结果。有关 K 的取值：

- 如果较大，相当于使用较大邻域中的训练实例进行预测，可以减小估计误差， 但是距离较远的样本也会对预测起作用，导致预测错误。

- 相反地，如果 K 较小，相当于使用较小的邻域进行预测，如果邻居恰好是噪 声点，会导致过拟合。

- 一般情况下，K 会倾向选取较小的值，并使用交叉验证法选取最优 K 值。
