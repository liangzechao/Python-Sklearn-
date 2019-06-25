# K-means方法及应用

## K-means聚类算法

k-means算法以k为参数，把n个对象分成k个簇，使簇内具有较高的相似度，而簇间的相似度较低。
其处理过程如下：
1.随机选择k个点作为初始的聚类中心；
2.对于剩下的点，根据其与聚类中心的距离，将其归入最近的簇
3.对每个簇，计算所有点的均值作为新的聚类中心
4.重复2、3直到聚类中心不再发生改变

![ZkX8C4.png](https://s2.ax1x.com/2019/06/24/ZkX8C4.png)

## K-means的应用

**数据介绍：**
现有1999年全国31个省份城镇居民家庭平均每人全年消费性支出的八个主要变量数据，这八个变量分别是：食品、衣着、家庭设备用品及服务、医疗保健、交通和通讯、娱乐教育文化服务、居住以及杂项商品和服务。利用已有数据，对31个省份进行聚类。
**实验目的：**
通过聚类，了解1999年各个省份的消费水平在国内的情况。
**技术路线**：[sklearn.cluster.Kmeans](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

## [数据实例：](https://github.com/liangzechao/PythonSklearnML/blob/master/3.聚类/3.1KMeans/city.txt)
1999年全国31个省份城镇居民家庭平均每人全年消费性支出数据

![ZkX2rt.png](https://s2.ax1x.com/2019/06/24/ZkX2rt.png)

## [实验代码](https://github.com/liangzechao/PythonSklearnML/blob/master/3.聚类/3.1KMeans/SpendingKMeans.py)

## KMeans参数
- n_clusters：即我们的k值，一般需要多试一些值以获得较好的聚类效果。
- init：即初始值选择的方式，可以为完全随机选择'random',优化过的'k-means++'或者自己指定初始化的k个质心。一般建议使用默认的'k-means++'。
- max_iter：最大的迭代次数，一般如果是凸数据集的话可以不管这个值，如果数据集不是凸的，可能很难收敛，此时可以指定最大的迭代次数让算法可以及时退出循环。
- n_init：用不同的初始化质心运行算法的次数。由于K-Means是结果受初始值影响的局部最优的迭代算法，因此需要多跑几次以选择一个较好的聚类效果，默认是10，一般不需要改。如果你的k值较大，则可以适当增大这个值。
- algorithm：有“auto”, “full” or “elkan”三种选择。"full"就是我们传统的K-Means算法， “elkan”是我们原理篇讲的elkan K-Means算法。默认的"auto"则会根据数据值是否是稀疏的，来决定如何选择"full"和“elkan”。一般数据是稠密的，那么就是 “elkan”，否则就是"full"。一般来说建议直接用默认的"auto"

## 实验结果

聚成2类：km = KMeans(n_clusters=2)

![ZkjdQs.png](https://s2.ax1x.com/2019/06/24/ZkjdQs.png)

聚成3类：km = KMeans(n_clusters=3)

![ZkjoTK.png](https://s2.ax1x.com/2019/06/24/ZkjoTK.png)

聚成4类：km = KMeans(n_clusters=4)

![ZkjHYD.png](https://s2.ax1x.com/2019/06/24/ZkjHYD.png)

