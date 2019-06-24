import numpy as np     #导入numpy工具包
from os import listdir #使用listdir模块，用于访问本地文件
from sklearn import neighbors   # KNN 模块

# 定义img2vector函数，将加载的32*32 的图片矩阵展开成一列向量
def img2vector(fileName):    
    retMat = np.zeros([1024],int) # 定义返回的矩阵，大小为1*1024
    fr = open(fileName)           # 打开包含32*32大小的数字文件 
    lines = fr.readlines()        # 读取文件的所有行
    for i in range(32):           # 遍历文件所有行
        for j in range(32):       # 并将01数字存放在retMat中     
            retMat[i*32+j] = lines[i][j]    
    return retMat

# 将样本标签转化为one-hot向量
def readDataSet(path):    
    fileList = listdir(path)    # 获取文件夹下的所有文件 
    numFiles = len(fileList)    # 统计需要读取的文件的数目
    dataSet = np.zeros([numFiles,1024],int) #用于存放所有的数字文件
    hwLabels = np.zeros([numFiles,10])      #用于存放对应的one-hot标签
    for i in range(numFiles):   #遍历所有的文件
        filePath = fileList[i]  #获取文件名称/路径      
        digit = int(filePath.split('_')[0])  #通过文件名获取标签      
        hwLabels[i][digit] = 1.0        #将对应的one-hot标签置1
        dataSet[i] = img2vector(path +'/'+filePath) #读取文件内容   
    return dataSet,hwLabels

#read dataSet
train_dataSet, train_hwLabels = readDataSet(r'D:\Workplace\sklearnML\2.分类\2.6手写识别\digits\trainingDigits')     # 改为数据文件路径

# 构建KNN分类器：设置查找算法以及邻居点数量(k)值。
# KNN是一种懒惰学习法，没有学习过程，只在预测时去查找最近邻的点，数据集的输入就是构建KNN分类器的过程。
# 构建KNN时我们同时调用了fit函数。
knn = neighbors.KNeighborsClassifier(algorithm='kd_tree', n_neighbors=3)
knn.fit(train_dataSet, train_hwLabels)

# read testing dataSet
dataSet,hwLabels = readDataSet(r'D:\Workplace\sklearnML\2.分类\2.6手写识别\digits\testDigits')  # 改为对应路径

# 测试集评价
res = knn.predict(dataSet)  #对测试集进行预测
error_num = np.sum(res != hwLabels) #统计分类错误的数目
num = len(dataSet)          #测试集的数目
print("Total num:",num," Wrong num:", \
      error_num,"  WrongRate:",error_num / float(num))