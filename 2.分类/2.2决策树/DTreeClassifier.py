from sklearn.datasets import load_iris                      #sklearn 内嵌的鸢尾花数据集
from sklearn.tree import DecisionTreeClassifier             #导入决策树分类器
from sklearn.model_selection import  cross_val_score        #导入计算交叉验 证值的函数 cross_val_score,用于验证K的大小


clf=DecisionTreeClassifier()                                #使用默认参数,创建一颗基于基尼系数的决策树,并将该决策树分类器赋值给变量clf
iris=load_iris()                                            #将鸢尾花数据赋值给变量 iris


#决策树分类器做为待评估的模型，iris.data鸢尾花数据做为特征，
# iris.target鸢尾花分类标签做为目标结果，通过设定cv为10，使用10折交叉验证。
#得到最终的交叉验证得分。
print(cross_val_score(clf,iris.data,iris.target,cv=10))
