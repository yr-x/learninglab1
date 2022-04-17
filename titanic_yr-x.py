# 데이터 가져오기
from configparser import MAX_INTERPOLATION_DEPTH
import pandas as pd
from sklearn.decomposition import randomized_svd

x_train = pd.read_csv('titanic_x_train.csv')
x_test = pd.read_csv('titanic_x_test.csv')
y_train = pd.read_csv('titanic_y_train.csv')

# 전처리 
x_test_passenger_id = x_test['PassengerId']
x_train = x_train.drop(columns = ['PassengerId'])
x_test = x_test.drop(columns = ['PassengerId'])
y_train = y_train.drop(columns = ['PassengerId'])
x_train = x_train.drop(columns = ['티켓번호'])
x_test = x_test.drop(columns = ['티켓번호'])
x_train = x_train.drop(columns = ['승객이름'])
x_test = x_test.drop(columns = ['승객이름'])
x_train = x_train.drop(columns = ['나이'])
x_test = x_test.drop(columns = ['나이'])
x_train = x_train.drop(columns = ['객실번호'])
x_test = x_test.drop(columns = ['객실번호'])

# 결측치 처리
x_train['선착장'] = x_train['선착장'].fillna('S')
x_test['선착장'] = x_test['선착장'].fillna('S')

# 인코딩
x_train['성별'] = x_train['성별'].replace('male',0).replace('female',1)
x_test['성별'] = x_test['성별'].replace('male',0).replace('female',1)
선착장_dummay = pd.get_dummies(x_train['선착장'], drop_first=True)\
    .rename(columns={'Q':'선착장Q', 'S':'선착장S'})
x_train = pd.concat([x_train, 선착장_dummay], axis = 1)
x_train = x_train.drop(columns = ['선착장'])
선착장_dummay = pd.get_dummies(x_test['선착장'], drop_first=True)\
    .rename(columns={'Q':'선착장Q', 'S':'선착장S'})
x_test = pd.concat([x_test, 선착장_dummay], axis = 1)
x_test = x_test.drop(columns = ['선착장'])

# 파생변수 
x_train['가족수'] = x_train['형제자매배우자수'] + x_train['부모자식수']
x_train = x_train.drop(columns=['형제자매배우자수','부모자식수'])
x_test['가족수'] = x_test['형제자매배우자수'] + x_test['부모자식수']
x_test = x_test.drop(columns=['형제자매배우자수','부모자식수'])

# 데이터 분리 
from sklearn.model_selection import train_test_split
X_TRAIN, X_TEST, Y_TRAIN, Y_TEST = \
    train_test_split(x_train, y_train, test_size = 0.2, randomized_state = 10)

# 모델 학습
from xgboost import XGBClassifier 
model = XGBClassifier(n_estimators = 100, max_depth = 5, eval_matric = 'error',\
    random_state = 10)
model.fit(X_TRAIN, Y_TRAIN)

# 최종 결과 저장 
y_test_prediccted = pd.DataFrame(model.predict(x_test)).\
    rename(columns = {0:'Survived'})
final = pd.concat([x_test_passenger_id, y_test_prediccted], axis = 1)
final.to_csv('titanic_modeling_yr-x.csv', index = False)

