# 朴素贝叶斯

朴素贝叶斯分类器是一个以贝叶斯定理为基础的多分类的分类器。 对于给定数据，首先基于特征的条件独立性假设，学习输入输出的联合概率分布，然后基于此模型，对给定的输入x，利用贝叶斯定理求出后验概率最大的输出y。

![VLsvY4.png](https://s2.ax1x.com/2019/06/18/VLsvY4.png)

在sklearn库中，实现了三个朴素贝叶斯分类器，如下表所示： 

[![VLyCOx.md.png](https://s2.ax1x.com/2019/06/18/VLyCOx.md.png)](https://imgchr.com/i/VLyCOx)

区别在于假设某一特征的所有属于某个类别的观测值符合特定分布，如，分类问题的特征包括人的身高，身高符合高斯分布，这类问题适合高斯朴素贝叶斯

在sklearn库中，可以使用[sklearn.naive_bayes.GaussianNB](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html)创建一个高斯 朴素贝叶斯分类器，其参数有：

- priors ：给定各个类别的先验概率。如果为空，则按训练数据的实际情况 进行统计；如果给定先验概率，则在训练过程中不能更改。


## [实例](https://github.com/liangzechao/PythonSklearnML/blob/master/2.分类/2.3朴素贝叶斯/BayesClassifier.py)