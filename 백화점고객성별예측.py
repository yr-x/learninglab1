# 데이터 불러오기
import pandas as pd
from pyrsistent import v

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

print(x_mainobj)
print(len(x_mainobj))
print(x_mainpla)
print(len(x_mainpla))

print(set(x['main_product'].unique()) - set(validation['main_product'].unique()))
print(set(x['where'].unique()) - set(validation['where'].unique()))

print(set(validation['main_product'].unique()) - set(x['main_product'].unique()))
print(set(validation['where'].unique()) - set(x['where'].unique()))

x[x['main_product'] == '소형가전']

x1 = x[x['main_product'] != '소형가전'].reset_index(drop = True)
y1 = y[(y['cust_id'] != 1521) & (y['cust_id'] != 2035)].reset_index(drop = True)

x1 = x1.drop('cust_id', axis = 1)
y1 = y1.gender
x2 = validation.drop('cust_id', axis = 1)

# 1-hote encoding 
x_dum = pd.get_dummies(x1)
validation_dum = pd.get_dummies(x2)

# 데이터 정규화 
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(x_dum)
x_dumm = sc.transform(x_dum)
validation_dumm = sc.transform(validation_dum)

# 데이터 7:3 분할
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(x_dumm, y1, test_size=0.3, random_state=60, stratify = y1)

# 모델학습 
from sklearn.metrics import roc_auc_score, roc_curve
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from xgboost import XGBClassifier

dt = DecisionTreeClassifier().fit(X_train, y_train)
probs_dt = dt.predict_proba(X_test)[:,1]
print('DecisionTreeClassifier:', roc_auc_score(y_test, probs_dt))
result_dt = roc_auc_score(y_test, probs_dt)

# lr = LogisticRegression().fit(X_train, y_train)
# probs_lr = lr.predict_proba(X_test[:,1])
# print('Logistic Regression:', roc_auc_score(y_test, probs_lr))
# result_lr = roc_auc_score(y_test, probs_lr)

rf = RandomForestClassifier().fit(X_train, y_train)
probs_rf = rf.predict_proba(X_test)[:,1]
print('RandomForestClassifier:', roc_auc_score(y_test, probs_rf))
result_rf = roc_auc_score(y_test, probs_rf)

xg = XGBClassifier().fit(X_train, y_train)
probs_xg = xg.predict_proba(X_test)[:,1]
print('XGBClassifier:', roc_auc_score(y_test, probs_xg))
result_xg = roc_auc_score(y_test, probs_xg)

prob_fin = rf.predict_proba(validation_dumm)[:,1]

submit = pd.concat([validation.cust_id, pd.DataFrame(prob_fin)], axis = 1)
submit.columns = ['cust_id', 'gender']

submit.to_csv('백화점고객성별예측.csv', index = False)
