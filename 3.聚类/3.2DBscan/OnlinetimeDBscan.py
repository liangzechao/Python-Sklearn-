import numpy as np
import sklearn.cluster as skc           # 导入聚类模块重命名为skc
from sklearn import metrics             # 模型评估模块
import matplotlib.pyplot as plt         # 可视化


mac2id=dict()                                                           # mac2id
onlinetimes=[]
f=open(r'D:\Workplace\sklearnML\3.聚类\3.2DBscan\TestData.txt',encoding='utf-8')
for line in f:
    mac=line.split(',')[2]                                              # 读取mac地址
    onlinetime=int(line.split(',')[6])                                  # 读取上网时长
    starttime=int(line.split(',')[4].split(' ')[1].split(':')[0])       # 读取开始上网时间
    if mac not in mac2id:
        mac2id[mac]=len(onlinetimes)                      # key是mac地址，value是对应mac地址的上网时长以及开始上网时间  
        onlinetimes.append((starttime,onlinetime))
    else:
        onlinetimes[mac2id[mac]]=[(starttime,onlinetime)]

# 数据提取后，mac2id字典为(mac，下标),onlinetimes为[starttime,onlinetime]

real_X=np.array(onlinetimes).reshape((-1,2))                # [starttime,onlinetime]

X=np.log(1+real_X[:,1:])                                             # 取onlinetime对数变换后训练

db=skc.DBSCAN(eps=0.14,min_samples=10).fit(X)               # 调用 DBSCAN 方法进行训练，半径0.14，邻域内的样本点数10
labels = db.labels_                                         # labels为每个数据的簇标签

print('Labels:')
print(labels)                                               # 打印数据被记上的标签
raito=len(labels[labels[:] == -1]) / len(labels)            # 计算标签 为-1，即噪声数据的比例。
print('Noise raito:',format(raito, '.2%'))

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)                     # 计算簇的个数

print('Estimated number of clusters: %d' % n_clusters_)                         # 打印
print("Silhouette Coefficient: %0.3f"% metrics.silhouette_score(X, labels))     # 评价聚类效果
 
for i in range(n_clusters_):
    print('Cluster ', i,':')                                                     # 簇号
    count = len(X[labels == i])                   # 每一个簇内的样本个数
    mean = np.mean(real_X[labels == i][:,1])     # 均值
    std = np.std(real_X[labels == i][:,1])       # 标准差
    print('\t number of sample:',count)
    print('\t mean of sample:',format(mean,'.1f'))
    print('\t std of sample:',format(std,'.1f'))


