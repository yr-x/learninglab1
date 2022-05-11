# 데이터 불러오기
import pandas as pd

x = pd.read_csv('X_train_2.csv')
y = pd.read_csv('y_train.csv')
validation = pd.read_csv('X_test_2.csv')

# 데이터 타입 확인 
x.dtypes
x.describe()

# 결측치 처리
x.isnull().sum()

x = x.fillna(0)
validation = validation.fillna(0)
validation.isnull().sum()

# 범주형 변수 0, 1 변환 
x_mainobj = x['main_product'].value_counts().index
x_mainpla = x['where'].value_counts().index

# print(x_mainobj)
# print(len(x_mainobj))
# print(x_mainpla)
# print(len(x_mainpla))

