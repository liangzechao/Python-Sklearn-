# DBSCAN方法及应用

## [DBSCAN密度聚类](https://baike.baidu.com/item/DBSCAN/4864716)

**DBSCAN算法是一种基于密度的聚类算法：**
- 聚类的时候不需要预先指定簇的个数
- 最终的簇的个数不定

**DBSCAN算法将数据点分为三类：**
- 核心点：在半径Eps内含有超过MinPts数目的点
- 边界点：在半径Eps内点的数量小于MinPts，但是落在核心点的邻域内
- 噪音点：既不是核心点也不是边界点的点

![ZArYE8.png](https://s2.ax1x.com/2019/06/24/ZArYE8.png)

**DBSCAN算法流程：**
1.将所有点标记为核心点、边界点或噪声点；
2.删除噪声点；
3.为距离在Eps之内的所有核心点之间赋予一条边；
4.每组连通的核心点形成一个簇；
5.将每个边界点指派到一个与之关联的核心点的簇中（哪一个核心点的半径范围之内）。

举例：有如下13个样本点，使用DBSCAN进行聚类

![ZArhvR.png](https://s2.ax1x.com/2019/06/24/ZArhvR.png)

取Eps=3，MinPts=3，依据DBSACN对所有点进行聚类（曼哈顿距离）。

![ZArHUO.png](https://s2.ax1x.com/2019/06/24/ZArHUO.png)

- 对每个点计算其邻域Eps=3内的点的集合。
- 集合内点的个数超过MinPts=3的点为核心点
- 查看剩余点是否在核心点的邻域内，若在，则为边界点，否则为噪声点。

![ZArX2d.png](https://s2.ax1x.com/2019/06/24/ZArX2d.png)

将距离不超过Eps=3的点相互连接，构成一个簇，核心点邻域内的点也会被加入到这个簇中。则右侧形成3个簇。

![ZAsSqP.png](https://s2.ax1x.com/2019/06/24/ZAsSqP.png)

## DBSCAN的应用实例

**数据介绍：**
现有大学校园网的日志数据，290条大学生的校园网使用情况数据，数据包括用户ID，设备的MAC地址，IP地址，开始上网时间，停止上网时间，上网时长，校园网套餐等。利用已有数据，分析学生上网的模式。

**实验目的：**
通过DBSCAN聚类，分析学生上网时间和上网时长的模式。

技术路线：[sklearn.cluster.DBSCAN](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.DBSCAN.html)

## 数据实例：

|学生上网日志|（单条数据格式） |
| ------ | ------ |
|记录编号| 2c929293466b97a6014754607e457d68|
|学生编号| U201215025|
|MAC地址 |A417314EEA7B|
|IP地址 |10.12.49.26|
|开始上网时间| 2014-07-20 22:44:18.540000000|
|停止上网时间 |2014-07-20 23:10:16.540000000|
|上网时长 |1558|

## 实验过程：
- 使用算法： DBSCAN聚类算法
- 实现过程：

![ZAs2eP.png](https://s2.ax1x.com/2019/06/24/ZAs2eP.png)

## [实验代码(starttime聚类)](https://github.com/liangzechao/PythonSklearnML/blob/master/3.聚类/3.2DBscan/StarttimeDBscan.py)

## [实验代码(onlinetime聚类)](https://github.com/liangzechao/PythonSklearnML/blob/master/3.聚类/3.2DBscan/OnlinetimeDBscan.py)