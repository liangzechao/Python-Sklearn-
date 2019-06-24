# 手写数字识别

## 1.概念介绍：

图像识别（Image Recognition）是指利用计算机对图像进行处理、分析和理解，以识别各种不同模式的目标和对像的技术。 

图像识别的发展经历了三个阶段：文字识别、数字图像处理与识别、物体识别。机器学习领域一般将此类识别问题转化为分类问题。

手写识别是常见的图像识别任务。计算机通过手写体图片来识别出图片中的字，与印刷字体不同的是，不同人的手写体风格迥异，大小不一， 造成了计算机对手写识别任务的一些困难。 

数字手写体识别由于其有限的类别（0~9共10个数字）成为了相对简单 的手写识别任务。DBRHD和MNIST是常用的两个数字手写识别数据集

## [2.数据介绍：](https://github.com/liangzechao/PythonSklearnML/blob/master/2.分类/2.6手写识别/digits.zip)

MNIST的下载链接：[http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)。

MNIST是一个包含数字0~9的手写体图片数据集，图片已归一化为以手写数 字为中心的28*28规格的图片。

MNIST由训练集与测试集两个部分组成，各部分 规模如下： 

- 训练集：60,000个手写体图片及对应标签 
- 测试集：10,000个手写体图片及对应标签

![ZC3nQ1.png](https://s2.ax1x.com/2019/06/23/ZC3nQ1.png)

DBRHD（Pen-Based Recognition of Handwritten Digits Data Set）是UCI的机器学习中心提供的数字手写体数据库： [https://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits ](https://archive.ics.uci.edu/ml/datasets/Pen-Based+Recognition+of+Handwritten+Digits)

DBRHD数据集包含大量的数字0~9的手写体图片，这些图片来源于44位不同的人的手写数字，图片已归一化为以手写数字为中心的32*32规格的图片。

DBRHD的训练集与测试 集组成如下：
- 训练集：7,494个手写体图片及对应标签，来源于40位手写者 
- 测试集：3,498个手写体图片及对应标签，来源于14位手写者

![ZC32yq.png](https://s2.ax1x.com/2019/06/23/ZC32yq.png)

已有许多模型在MNIST或DBRHD数据集上进行了实验，有些模型对数据集进行了偏斜
矫正，甚至在数据集上进行了人为的扭曲、偏移、缩放及失真等操作以获取更加多样性的
样本，使得模型更具有泛化性。

- 常用于数字手写体的分类器：
1） 线性分类器 
2） K最近邻分类器
3） Boosted Stumps 
4） 非线性分类器
5） SVM 
6） 多层感知器
7） 卷积神经网络

后续任务：利用全连接的神经网络实现手写识别的任务

## 3.神经网络任务过程：

![ZC8YAU.png](https://s2.ax1x.com/2019/06/23/ZC8YAU.png)

- 输入
![ZCGM5D.png](https://s2.ax1x.com/2019/06/23/ZCGM5D.png)

- 输出
![ZCGlPe.png](https://s2.ax1x.com/2019/06/23/ZCGlPe.png)

- MPL的结构
![ZCGtqP.png](https://s2.ax1x.com/2019/06/23/ZCGtqP.png)

- 步骤
本实例的构建步骤如下：
步骤1：建立工程并导入sklearn包
步骤2：加载训练数据
步骤3：训练神经网络,利用[sklearn.neural_network.MLPClassifier()](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)
步骤4：测试集评价

## [4.神经网络代码](https://github.com/liangzechao/PythonSklearnML/blob/master/2.分类/2.6手写识别/HandWritingMLP.py)

## 5.神经网络实验效果

**隐藏层神经元个数影响：**
运行隐藏层神经元个数为50、100、200的多层感知机，对比实验效果：

![ZCJq6s.png](https://s2.ax1x.com/2019/06/23/ZCJq6s.png)

- 随着隐藏层神经元个数的增加，MLP的正确率持上升趋势；
- 大量的隐藏层神经元带来的计算负担与对结果的提升并不对等，因此，如何选取合适的隐藏神经元个数是一个值得探讨的问题。

**迭代次数影响分析:**
我们设隐藏层神经元个数为100，初始学习率为0.0001，最大迭代次数分别为500、
1000、1500、2000, 结果如下：

![ZCY6EV.png](https://s2.ax1x.com/2019/06/23/ZCY6EV.png)
- 过小的迭代次数可能使得MLP早停，造成较低的正确率。
- 当最大迭代次数>1000时，正确率基本保持不变，这说明MLP在第1000迭代时已收敛，剩余的迭代次数不再进行。
- 一般设置较大的最大迭代次数来保证多层感知机能够收敛，达到较高的正确率。

**学习率影响分析：**
改用随机梯度下降优化算法即将MLPclassifer的参数（ solver='sgd', ），设隐藏层
神经元个数为100，最大迭代次数为2000，学习率分别为：0.1、0.01、0.001、0.0001，
结果如下：

![ZCt9VP.png](https://s2.ax1x.com/2019/06/23/ZCt9VP.png)

**结论**：较小的学习率带来了更低的正确率，这是因为较小学习率无法在2000次迭代内完成收敛，而步长较大的学习率使得MLP在2000次迭代内快速收敛到最优解。因此，较小的学习率一般要配备较大的迭代次数以保证其收敛。


## 6.KNN任务过程
- 本实例利用sklearn来训练一个K最近邻（ k-Nearest Neighbor ，KNN）分类器，用于识别数据集DBRHD的手写数字。
- 比较KNN的识别效果与多层感知机的识别效果。

本实例的构建步骤如下：
步骤1：建立工程并导入sklearn包
步骤2：加载训练数据
步骤3：构建KNN分类器,利用[sklearn.neighbors.KNeighborsClassifier()](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
步骤4：测试集评价

![ZPLW9I.png](https://s2.ax1x.com/2019/06/23/ZPLW9I.png)

## [7.KNN代码](https://github.com/liangzechao/PythonSklearnML/blob/master/2.分类/2.6手写识别/HandWritingKNN.py)

## 8.KNN实验效果

邻居数量K影响分析：设置K为1、3、5、7的KNN分类器，对比他们的实验效果

![ZPOcrT.png](https://s2.ax1x.com/2019/06/23/ZPOcrT.png)

K=3时正确率最高，当K>3时正确率开始下降，这是由于当样本为稀疏数据集时（本实例只有946个样本），其第k个邻居点可能与测试点距离较远，因此投出了错误的一票进而影响了最终预测结果。

## 9.对比实验

**KNN分类器vs.多层感知机:**
我们取在上节对不同的隐藏层神经元个数、最大迭代次数、学习率进行的各个对比实验中准确率最高（H）与最差（L）的MLP分类器来进行对比，其各个MLP的参数设置如下

![ZPji11.png](https://s2.ax1x.com/2019/06/23/ZPji11.png)

将效果最好的KNN分类器（K=3）和效果最差的KNN分类器（K=7）与各个MLP分类器作对比如下：

![ZPjGB8.png](https://s2.ax1x.com/2019/06/23/ZPjGB8.png)

**结论：**
- KNN的准确率远高于MLP分类器，这是由于MLP在小数据集上容易过拟合的原因。
- MLP对于参数的调整比较敏感，若参数设置不合理，容易得到较差的分类效果，因此参数的
设置对于MLP至关重要。
