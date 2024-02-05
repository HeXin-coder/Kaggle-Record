# 导入pandas 方便数据读取和预处理
import pandas as pd

# 分别对训练和测试数据从本地进行读取
train = pd.read_csv('../Datasets/titanic/train.csv')
test = pd.read_csv('../Datasets/titanic/test.csv')

# 先分别输出训练与测试数据的基本信息（可通过这种方式对数据的规模、各个特征的数据类型以及是否有缺失等，有一个总体的了解）
print train.info()
print test.info()
