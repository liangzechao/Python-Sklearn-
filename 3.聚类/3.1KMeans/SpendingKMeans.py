import numpy as np
from sklearn.cluster import KMeans                  # KMeans 模块
 
 
def loadData(filePath):
    fr = open(filePath,'r+')                                            # r+：读写打开一个文本文件,https://www.runoob.com/python/python-func-open.html
    lines = fr.readlines()                                              # .readlines() 一次读取整个文件（类似于 .read() ) , https://www.runoob.com/python/file-readlines.html
    retData = []                                                        # retCityName：用来存储城市名称
    retCityName = []                                                    # retData：用来存储城市的各项消费信息
    for line in lines:
        items = line.strip().split(",")
        retCityName.append(items[0])
        retData.append([float(items[i]) for i in range(1,len(items))])
    return retData,retCityName                                          # 返回值：返回城市名称，以及该城市的各项消费信息
 

if __name__ == '__main__':
    data,cityName = loadData(r'D:\Workplace\sklearnML\3.聚类\3.1KMeans\city.txt')       # 利用loadData方法读取数据，改为相应路径
    km = KMeans(n_clusters=4)                                                           # 创建实例进行聚类，聚成4簇
    label = km.fit_predict(data)                                                        # 调用Kmeans()fit_predict()方法进行计算，label记录data每一数组的分类，结果：[3 1 0 0 0 0 0 0 3 2 1 2 1 0 0 0 2 2 3 2 2 1 2 0 2 1 0 0 0 0 0]
    expenses = np.sum(km.cluster_centers_,axis=1)
    #print(expenses)
    CityCluster = [[],[],[],[]]                                                         # 按聚类参数改
    for i in range(len(cityName)):                                                      # 按城市个数遍历
        CityCluster[label[i]].append(cityName[i])                                       # 各簇添加城市名称，label[0],label[1],label[2],label[3]
    for i in range(len(CityCluster)):                                                   # 遍历4簇
        print("Expenses:%.2f" % expenses[i])
        print(CityCluster[i])                                                           # 输出各簇城市



# 调用KMeans方法所需参数
# n_clusters：用于指定聚类中心的个数
# init：初始聚类中心的初始化方法
# max_iter：最大的迭代次数
# 一般调用时只用给出n_clusters即可，init默认是k-means++，max_iter默认是300
# 其它参数：
# data：加载的数据
# label：聚类后各数据所属的标签
# axis: 按行求和
# fit_predict()：计算簇中心以及为簇分配序号