# Q. 고객 3,500명에 대한 학습용 데이터(y_train.csvm X_train.csv)를 이용하여 성별예측 모형을 만든 후, 
# 이를 평가용 데이터(X_test.csv)에 적용하여 얻은 2,482명 고객의 성별 예측값(남자일 확률)을 CSV 파일로 생성하시오. 'cust_id', 'gender'
# 제출한 모델의 성능은 ROC-AUC 평가지표에 따라 채점한다.

# 데이터 불러오기
import pandas as pd
from pyrsistent import v

x = pd.read_csv('X_train_2.csv')
y = pd.read_csv('y_train.csv')
validation = pd.read_csv('X_test_2.csv')

# 데이터 타입 확인 (EDA)
# print(x.dtypes)
# print(x.describe())
# print(validation.describe())
# print(x.head())

# # 결측치 처리
print(x.isnull().sum())
x = x.fillna(0)
validation = validation.fillna(0)
validation.isnull().sum()

# # 범주형 변수 0, 1 변환 
x_mainobj = x['main_product'].value_counts().index
print(x_mainobj)
print(len(x_mainobj))
x_mainpla = x['where'].value_counts().index
print(x_mainpla)
print(len(x_mainpla))

print(set(x['main_product'].unique()) - set(validation['main_product'].unique()))
print(set(x['where'].unique()) - set(validation['where'].unique()))

print(set(validation['main_product'].unique()) - set(x['main_product'].unique()))
print(set(validation['where'].unique()) - set(x['where'].unique()))

print(x[x['main_product'] == '소형가전'])

x1 = x[x['main_product'] != '소형가전'].reset_index(drop = True)
y1 = y[(y['cust_id'] != 1521) & (y['cust_id'] != 2035)].reset_index(drop = True)

# 모델링에 필요없는 열 삭제 
x1 = x1.drop('cust_id', axis = 1)
y1 = y1.gender
x2 = validation.drop('cust_id', axis = 1)

# # 1-hote encoding 
x_dum = pd.get_dummies(x1)
print(x_dum)
validation_dum = pd.get_dummies(x2)
print(validation_dum)

# 데이터 정규화 
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
sc.fit(x_dum)
x_dumm = sc.transform(x_dum)
validation_dumm = sc.transform(validation_dum)
print(x_dumm)

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

# 랜덤포레스트 모델 적용하여 남자일 확률 결과 
prob_fin = rf.predict_proba(validation_dumm)[:,1]
print(prob_fin)

# csv 파일 생성 
submit = pd.concat([validation.cust_id, pd.DataFrame(prob_fin)], axis = 1)
submit.columns = ['cust_id', 'gender']
submit.to_csv('백화점고객성별예측.csv', index = False)
