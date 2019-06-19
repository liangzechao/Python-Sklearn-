from sklearn.neighbors import KNeighborsClassifier          #导入K近邻分类器


X=[[0],[1],[2],[3]]                                         #创建一组数据X和它对应的标签y
y=[0,0,1,1]

#参数 n_neighbors设置为 3，即使用最近的3个邻居作为分类的依据，
# 其他参数保持默认值，并将创建好的实例赋给变量 neigh。
neigh =KNeighborsClassifier(n_neighbors=3)


#调用 fit() 函数，将训练数据X和标签y送入分类器进行学习
neigh.fit(X,y)

#调用 predict() 函数，对未知分类样本[1.1] 分类，
#可以直接并将需要分类的数据构造为数组形式作为参数传入得到分类标签作为返回值。
print(neigh.predict([[1.1]]))


# [0]
# 样例输出值是 0，表示K近邻分类器通过计算样本 [1.1]与训练数据的距离,
# 取 0,1,2 这 3 个邻居作为依据，根据“投票法”最终将样本分为类别 0。