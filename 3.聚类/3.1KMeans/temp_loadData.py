import numpy as np
from sklearn.cluster import KMeans

fr = open(r'D:\Workplace\sklearnML\3.聚类\3.1KMeans\city.txt','r+')                                            # r+：读写打开一个文本文件,https://www.runoob.com/python/python-func-open.html
lines = fr.readlines()                                              # .readlines() 一次读取整个文件（类似于 .read() ) , https://www.runoob.com/python/file-readlines.html
retData = []                                                        # retCityName：用来存储城市名称
retCityName = []                                                    # retData：用来存储城市的各项消费信息
for line in lines:
    items = line.strip().split(",")
    retCityName.append(items[0])
    retData.append([float(items[i]) for i in range(1,len(items))])
print(retData,retCityName) 