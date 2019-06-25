# 无监督学习

## 无监督学习的目标

利用无标签的数据学习数据的分布或数据与数据之间的关系被称作无监督学习。
- 有监督学习和无监督学习的最大区别在于数据是否有标签
- 无监督学习最常应用的场景是聚类(clustering)和降维(Dimension Reduction)

## 聚类(clustering)

聚类(clustering)，就是根据数据的“相似性”将数据分为多类的过程。

评估两个不同样本之间的“相似性” ，通常使用的方法就是计算两个样本之间的“距离”。使用不同的方法计算样本间的距离会关系到聚类结果的好坏。

![Zk8hbn.png](https://s2.ax1x.com/2019/06/24/Zk8hbn.png)

## 欧氏距离
欧氏距离是最常用的一种距离度量方法，源于欧式空间中两点的距离。
其计算方法如下：
<!-- $$ d = \sqrt{\sum_{k=1}^{n}({X_{1k}}-{X_{2k}})^2} $$ -->

![ZkGRJK.png](https://s2.ax1x.com/2019/06/24/ZkGRJK.png)

![ZkGHot.png](https://s2.ax1x.com/2019/06/24/ZkGHot.png)

## 曼哈顿距离

曼哈顿距离也称作“城市街区距离”，类似于在城市之中驾车行驶，从一个十字路口到另外一个十字楼口的距离。

通俗来讲，想象你在曼哈顿要从一个十字路口开车到另外一个十字路口，驾驶距离是两点间的直线距离吗？显然不是，除非你能穿越大楼。而实际驾驶距离就是这个“曼哈顿距离”，此即曼哈顿距离名称的来源，同时，曼哈顿距离也称为城市街区距离(City Block distance)。

其计算方法如下：

<!-- $$ d = \sum_{k=1}^{n}\left |{X_{1k}}-{X_{2k}} \right | $$ -->

![ZkNZ6S.png](https://s2.ax1x.com/2019/06/24/ZkNZ6S.png)

![ZkNKTs.png](https://s2.ax1x.com/2019/06/24/ZkNKTs.png)

## 马氏距离

马氏距离表示数据的协方差距离，是一种尺度无关的度量方式。也就是说马氏距离会先将样本点的各个属性标准化，再计算样本间的距离。

**马氏距离的优缺点：** 量纲无关，排除变量之间的相关性的干扰。

其计算方式如下：（s是协方差矩阵，如图）

<!-- $$ d(x_i,x_j) = \sqrt{(x_i - x_j)^Ts^{-1}(x_i - x_j)} $$ -->

![ZkNqBQ.png](https://s2.ax1x.com/2019/06/24/ZkNqBQ.png)

![ZkNXAs.png](https://s2.ax1x.com/2019/06/24/ZkNXAs.png)

## 夹角余弦

余弦相似度用向量空间中两个向量夹角的余弦值作为衡量两个样本差异的大小。余弦值越接近1，说明两个向量夹角越接近0度，表明两个向量越相似。其计算方法如下：

<!-- $$ \cos(\theta)=\frac{\sum_{k=1}^{n}{X_{1k}}{X_{2k}}}{\sqrt{\sum_{k=1}^{n}{X^2_{1k}}}\sqrt{\sum_{k=1}^{n}{X^2_{2k}}}} $$ -->
![ZkaQzV.png](https://s2.ax1x.com/2019/06/24/ZkaQzV.png)

![ZkaJZ4.png](https://s2.ax1x.com/2019/06/24/ZkaJZ4.png)

## Sklearn vs. 聚类
- scikit-learn库（以后简称sklearn库）提
供的常用聚类算法函数包含在[sklearn.cluster](https://scikit-learn.org/stable/modules/classes.html#module-sklearn.cluster)这个模块中，如：[K-Means](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans)，近邻传播算法([AffinityPropagation](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.AffinityPropagation.html#sklearn.cluster.AffinityPropagation))，[DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html#sklearn.cluster.DBSCAN)，等。

- 以同样的数据集应用于不同的算法，可能会得到不同的结果，算法所耗费的时间也不尽相同，这是由算法的特性决定的。

下图是我们调用sklearn库的标准函数对不同数据集执行的聚类结果。
![Zkdu0e.png](https://s2.ax1x.com/2019/06/24/Zkdu0e.png)

**sklearn.cluster模块提供的各聚类算法函数可以使用不同的数据形式作为输入:**
- 标准数据输入格式:[样本个数，特征个数]定义的矩阵形式。
- 相似性矩阵输入格式：即由[样本数目，样本数目]定义的矩阵形式，矩阵中的每一个元素为两个样本的相似度，如DBSCAN， AffinityPropagation(近邻传播算法)接受这种输入。如果以余弦相似度为例，则对角线元素全为1. 矩阵中每个元素的取值范围为[0,1]。



|算法名称|参数|可扩展性|相似性度量|
| ------ | ------ | ------ | ------ |
|K-means| 聚类个数 | 大规模数据| 点间距离 |
|DBSCAN| 邻域大小| 大规模数据| 点间距离|
|Gaussian Mixtures|聚类个数及其他超参|复杂高不适合处理大规模数据|马氏距离|
|Birch|分支因子，阈值等其他超参|大规模数据|两点间的欧式距离|