import numpy as np
from sklearn.naive_bayes import GaussianNB                      #导入朴素贝叶斯分类器


X=np.array([[-1,-1],[-2,-1],[-3,-2],[1,1],[2,1],[3,2]])
Y=np.array([1,1,1,2,2,2])

clf = GaussianNB(priors=None)                   #使用默认参数，创建一个高斯朴素贝叶斯分类器，并将该分类器赋给变量clf

clf.fit(X,Y)                                    #使用fit()函数进行训练，并使用predict()函数进行预测

print(clf.predict([[-0.8,-1],[0,-1]]))          #测试时可以构造二维数组达到同时预测多个样本的目的

