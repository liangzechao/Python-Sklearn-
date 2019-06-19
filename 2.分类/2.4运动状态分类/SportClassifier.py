import numpy as np
import pandas as pd

from sklearn.preprocessing import Imputer               #导入预处理模块
from sklearn.model_selection import  train_test_split   #导入自动生成训练集和测试集的模块train_test_split
from sklearn.metrics import classification_report       #导入预测结果评估模块classification_report

#从sklearn库中依次导入三个分类器模
from sklearn.neighbors import KNeighborsClassifier      # KNN
from sklearn.tree import DecisionTreeClassifier         # 决策树
from sklearn.naive_bayes import  GaussianNB             # 朴素贝叶斯

#数据导入函数,参数时特征文件的列表feature_paths和标签 文件的列表label_paths
def load_dataset(feature_path,label_paths):             #读取特征文件列表和标签文件列表中的内容，规定后返回
    
    feature = np.ndarray(shape=(0, 41))                 #定义feature数组变量，列数量和特征维度一致为41，有41列数据
    label = np.ndarray(shape=(0, 1))                    #定义空的标签变量，列数量与标签维度一致为1
    for file in feature_path:
        #使用逗号分隔符读取特征数据，将问号替换标记为缺失值，文件中不包含表头
        #使用pandas库的read_table函数读取一个特征文件的内容，
        # 其中指定分隔符为逗号、缺失值为问号且 文件不包含表头行。
        df =pd.read_table(file, delimiter=',',na_values='?',header=None)
        
        imp =Imputer(missing_values='NaN',strategy='mean',axis=0)           #使用平均值补全缺失值，然后将数据进行补全
        imp.fit(df)
        df =imp.transform(df)
        feature=np.concatenate((feature,df))                                #将新读入的数据合并到特征集中
    for file in label_paths:
        
        df=pd.read_table(file,header=None)                                  #读取标签数据，文件中不包含表头
        label =np.concatenate((label,df))                                   #将新读入的数据合并到标签集合中
    #将标签规整为一维向量
    label=np.ravel(label)
    return feature,label
    
if __name__ == '__main__':
    #设置数据路径
    featurePaths = ['./data/A.feature', './data/B.feature', './data/C.feature', './data/D.feature', './data/E.feature']
    labelPaths = ['./data/A.label', './data/B.label', './data/C.label', './data/D.label', './data/E.label']
    load_dataset(featurePaths[:4],labelPaths[:4])

    #将前4个数据作为训练集读入
    x_train,y_train = load_dataset(featurePaths[:4],labelPaths[:4])
    #将最后一个作为测试集读入
    x_test,y_test =load_dataset(featurePaths[4:],labelPaths[4:])
    #使用全量数据作为训练集，借助train_text_split函数将数据打乱
    x_train,x_,y_train,y_ =train_test_split(x_train,y_train,test_size=0.0)

    # 使用默认参数创建K近邻分类器，并将训练集x_train和y_train送入fit()函数进行训练，
    # 训练后的分类器保存到变量knn中。
    print("Start training knn")
    knn = KNeighborsClassifier().fit(x_train,y_train)
    print("Training done!")
    answer_knn = knn.predict(x_test)
    print("Prediction done")

    
    #使用默认参数创建决策树分类器dt，并将训练集x_train和y_train送入fit()函数进行训练。
    # 训练后的分类器保存到变量dt中
    print("Start training DT")
    dt=DecisionTreeClassifier().fit(x_train,y_train)
    print("Training done!")
    answer_dt=dt.predict(x_test)
    print("Prediction done")


    #使用默认参数创建贝叶斯分类器，并将训练集x_train和y_train送入fit()
    #函数进行训练。训练后的分类器保存到变量gnb中
    print("Start training Bayes")
    gnb =GaussianNB().fit(x_train,y_train)
    print("Training done!")
    answer_gnb=gnb.predict(x_test)
    print("Prediction done")

    #计算准确率与召回率
    print("\n\nThe classifiction report for knn:")
    print(classification_report(y_test,answer_knn))

    print("\n\nThe classifiction report for dt:")
    print(classification_report(y_test, answer_dt))

    print("\n\nThe classifiction report for gnb:")
    print(classification_report(y_test, answer_gnb))
