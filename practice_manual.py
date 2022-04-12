# 환경 설정 
# Git Bash 실행 
    # git config --global user.name "이름"
    # git config --global user.email "이메일 주소"
# VSCode 실행
    # New File 생성 
    # 파일명은 practice_닉네임.py 
    # 적당한 폴더에 저장 <- 앞으로 변경하지 않습니다 
    # git init 
    # git remote add origin https://github.com/yr-x/learninglab1.git
    # git add 파일명 또는 git add .
    # git commit -m "제출합니다"  
    # git push origin main 
    # git pull origin main (conflict 오류 발생 시) 


# 학습시작 
print("hello world") # hello world

# 연산자 
print(2 + 3 * 4) #14
print((2 + 3) * 4) #20
number = 2 + 3 * 4 #14
print(number)
number = number + 2 #16
print(number)
number += 2 #18
print(number)
number *= 2 #36
print(number)
number /=2 #18
print(number)
number -= 2 #16
print(number)
number %= 5 #1 나머지
print(number)

# 변수
animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집" + animal + "의 이름은" + name + "예요")
hobby = "공놀이"
print(name,"는 ", age, "살이며", hobby, "을 아주 좋아해요")
print(name+ "는 어른일까요?" + str(is_adult))


# Q1. 변수를 이용하여 다음 문장을 출력하시오
# 변수명: Station
# 변수값: "사당", "신도림", "인천공항" 순서대로 입력
# 출력문장: xx행 열차가 들어오고 있습니다. 
station = "신도림"
print(station + "행 열차가 들어오고 있습니다")


# 숫자처리함수 
print(abs(-5)) #5 절대값
print(pow(4, 2)) #4^2 제곱
print(max(5, 12)) #12 최대값
print(min(5, 12)) #5 최소값 
print(round(3.14)) #3 반올림 
print(round(4.99)) #5

from ipaddress import NetmaskValueError
from math import *
from sys import breakpointhook
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 4

# 랜덤함수 
from random import *
print(random()) #0~1 임의값
print(random() * 10) # 0~10
print(int(random() * 10)) # 0~10 정수 임의값
print(int(random() * 10) + 1) #1~10 정수 임의값 
print(randrange(1, 26)) #1~45 정수 임의값 
print(randint(1, 45)) #1~45 정수 임의값 

# Q2. 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다. 
# 월 4회 스터디를 하는데 3번은 온라인, 1번은 오프라인으로
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성

# 조건1 랜덤으로 날짜를 뽑아야함
# 조건2 월별 날짜는 다름을 감안하여 최소 일수인 28 이내로 정함
# 조건3 매월 1~3일은 스터디를 준비해야하므로 제외

# 출력물 예제
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

# 문자열처리함수 
from random import *
date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "선정되었습니다")


sentence = "나는 소년입니다"
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2) 
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

jumin = "990120-1234567"
print("성별 :" + jumin[7])
print("연 :" +jumin[0:2]) # 0~2직전까지 (0,1)
print("월 :" + jumin[2:4])
print("일 :" + jumin[4:6])
print("생년월일 :" + jumin[:6]) # 처음부터 6 직전까지
print("뒤 7자리" + jumin[7:]) # 7부터 끝까지 
print("뒤 7자리 (뒤에서부터) :" + jumin[-7:]) #뒤에서 7부터 끝까지

python = "Python is Amazing"
print(python.lower()) # python is amazing
print(python.upper()) #PYTHON IS AMAZING
print(python[0].isupper()) #true
print(len(python)) #17 문자열 길이
print(python.replace("Python", "Java"))

index = python.index("n") #5
print(index)
index = python.index("n", index + 1) # 두번째 n 위치 
print(python.find("Java")) #값이 없으면 -1
# print(python.index("Java")) #값이 없으면 에러 발생
print(python.count("n"))


# 문자열포맷
print("나는 %d살입니다" % 20) # d는 정수값만 
print("나는 %s을 좋아해요" % "파이썬") # s는 문자
print("Apple은 %c로 시작해요" % "A") 
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))
print("나는 {age}살이며, {color}색을 좋아햏요".format(age = 20, color = "빨간"))

age = 20 
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출문
print("백문이 불여일견 \n백견이 불여일타") # \n 줄바꿈
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.") # \" \' 문장 내에서 따옴표
print ("C:\\Users\\2920513\\Hyundai Motor and Kia\\My Document\\PythonWorkbook\\practice_manual.py") # \\문장 내에서 \
print("Red Apple\rPine") # \r 커서를 맨앞으로 이동 
print("Redd\bApple") # \b 백스페이스 한글자 삭제 
print("Red\tApple") # \t 탭

# Q3. 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 예) http://naver.com
# 규칙1 http:// 부분은 제외 => naver.com
# 규칙2 처음 만나는 점(.) 이후 부분은 제외 => Naver
# 규칙3 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e' 갯수 + "!"로 구성
# 예) 생성 비밀번호 nav51!
url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙1
print(my_str)
my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0~5 직전까지 0,1,2,3,4
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))

# 리스트 []
# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
# 조세호씨가 몇 번째 칸에 타고 있는가
print(subway.index("조세호")) # 1
#하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)
# 정형돈씨를 유재석 / 조세호 사이에 태워봄
subway.insert(1, "정형돈")
#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway.pop())
print(subway.pop())
print(subway)
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway.count("유재석"))
# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)
# 순서 뒤집기 가능
num_list.reverse()
print(num_list)
# 모두 지우기
num_list.clear()
print(num_list)
# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)
# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# 사전 { }
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
# print(cabinet[5]) # 값 없음 프로그램 오류 종료
print(cabinet.get(5)) # 값 없음 None 출력 프로그램 지속
print(cabinet.get(5, "사용 가능"))
print("hi")

print(3 in cabinet) #true
print(5 in cabinet) #false

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
# 새 손님
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 떠난 손님
del cabinet["A-3"]
# key, value 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
cabinet.clear()

# 튜플 (변경되지 않는 목록, 리스트보다 빠름)
menu = ("돈까스", "치즈까스")
print(menu[0])
# menu.add("생선까스") 함수 이용 불가 
# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)

# 세트 (중복 안됨, 순서없음)
my_set = {1,2,3,3,3}
print(my_set)
java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])
# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))
# 합집합 (java하거나 python 할 수 있는 개발자)
print(java | python)
print(java.union(python))
# 차집합 (java할 수 있지만 python 할줄 모르는 개발자)
print(java - python)
print(java.difference(python))
# python 할줄 아는 사람이 늘어남
python.add("김태호")
print(python)
# java를 잊어버림
java.remove("김태호")
print(java)

# 자료 구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # class 'set'
menu = list(menu)
print(menu, type(menu))
menu = tuple(menu)
print(menu, type(menu))
menu = set(menu)
print(menu, type(menu))

# Q4. 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글을 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오.

# 조건1: 편의상 댓글은 20명이 작성하였고 아이디는 1~20이라고 가정
# 조건2: 댓글 내용과 상관없이 무작위로 추첨하되 중복 불가
# 조건3: random 모듈의 shuffle과 sample을 활용
# (출력 예제)
# --당첨자 발표--
# 치킨 당첨자: 1
# 커피 당첨자: [2,3,4]
# --축하합니다--
# 활용 예제

from random import * 
users = range(1, 21) # 1부터 20까지 숫자 생성
users = list(users) # 리스트로 변경 
print(users)
shuffle(users)
print(users)
winners = sample(users, 4) 
print(winners)
print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다--")

# if
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or weather =="눈":
    print("우산을 챙기세요")
elif weather == "미세먼지": 
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지마세요")
elif 10 <= temp and temp <30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp <10:
    print("외투를 챙기세요")
else:
    print("너무 추워요 나가지 마세요")

# for
# 대기번호 1~4
for waiting_no in range(1, 6): # 0,1,2,3,4,5
    print("대기번호 : {0}".format(waiting_no))
starbucks = ["아이언맨","토르","그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))

# while 조건 만족할때까지 반복 
customer = "토르"
index = 5
while index >=1:
    print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다")

# customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비되었습니다. 호출 {1}회". format(customer, index))
#     index += 1
# 무한루프, ctrl+C 강제종료

customer = "토르"
person = "unknown"

while person != customer :
    print("{0}, 커피가 준비되었습니다".format(customer))
    person = input("이름이 어떻게 되세요 ")


# continue, break
absent = [2, 5] # 결석
no_book = [7] #책을 깜빡했음
for student in range(1, 11): # 1~10
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 반복문 탈출
    print("{0}, 책을 읽어봐".format(student))

# for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
students = {1,2,3,4,5}
print(students)
students = [i+100 for i in students]

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students)


# Q5. 당신은 Cocoa 서비스를 이용하는 택시 기사입니다.
# 50명의 승객과 매칭 기회가 있을 때 총 탑승 승객 수를 구하는 프로그램을 작성하시오
# 조건1: 승객별 운행 소요 시간은 5분~50분 사이의 난수로 정해집니다.
# 조건2: 당신은 소요 시간 5분~15분 사이의 승객만 매칭해야 합니다

# (출력문 예제)
# [0] 1번째 손님 (소요시간: 15분)
# [ ] 2번째 손님 (소요시간: 50분)
# [0] 3번째 손님 (소요시간: 5분)
# ...
# [ ] 50번째 손님 (소요시간: 16분)
# 총 탑승 승객 : 2분

from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1, 51): #1~50 승객
    time = randrange(5, 51) # 5분~50분 소요 시간
    if 5 <= time <= 15: # 5분
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우 
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0} 분".format(cnt))


# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다")

def deposit(balance, money): 
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money: # 잔액이 출금보다 많으면 
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance - money))
        return balance - money
    else: 
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance

balance = 0 # 잔액
balance = deposit(balance, 1000)
print(balance)
balance = withdraw(balance, 500)

def withdraw_night(balance, money): # 저녁에 출금
    commission = 100 # 수수료 100원
    return commission, balance - money - commission 
balance = 0
balance = deposit(balance, 1000)
comission, balance = withdraw_night(balance, 500)
print("수수료 {0}원이며, 잔액은 {1}원입니다.".format(comission, balance))


# 기본값

def profile(name, age, main_lang):
    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))
profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age=17, main_lang="파이썬"):
    print("이름: {0}\t나이 : {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))
    
profile("유재석")
profile("김태호")

# 키워드값 
def profile(name, age, main_lang):
    print(name, age, main_lang)
profile(name="유재석", main_lang="파이썬", age=20)

# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름: {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "python", "java", "C", "C++", "C#", "javaScript")
profile("김태호", 25, "Kotlin", "swift", "", "", "")

# 지역변수와 전역변수
gun = 10
def checkpoint(soldiers): #경계근무
    global gun # 전역 공간에 있는 gun 사용 
    gun = gun - soldiers 
    print("[함수 내] 남은 총: {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {0}".format(gun))
    return gun 

print("전체 총: {0}".format(gun))
checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총: {0}".format(gun))

# Q6. 표준 체중을 구하는 프로그램을 작성하시오
# * 표준 체중: 각 개인의 키에 적당한 체중
# (성별에 따른 공식)
# 남자: 키(m) x 키(m) + 22
# 여자: 키(m) x 키(m) + 21
# 조건1: 표준 체중은 별도의 함수 내에서 계산
# * 함수명: std_weight
# * 전달값: 키(height), 성별(gender)
# 조건2: 표준체중은 소수점 둘째자리까지 표시
# (출력 예제)
# 키 175cm 남자의 표준 체중은 67.38kg 입니다.

def std_weight(height, gender): # 키 m 단위 (실수), 성별 "남자"/"여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)
print(weight)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

# 표준입출력
print("Python", "Java", "JavaScript", sep="vs", end="?")
print("무엇이 더 재밌을까요?")

import sys
print("python","Java", file=sys.stdout)
print("python","Java", file=sys.stderr)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): 
    print(subject.ljust(8), str(score).rjust(4), sep=":") # 왼오정렬, 8/4공간 확보

# 은행 대기순번표
for num in range(1,21):
    print("대기번호 :" + str(num).zfill(3))  # 001, 002~020

answer = input("아무 값이나 입력하세요 : ") 
print(type(answer)) # 문자열 형태로만 저장됨
print("입력하신 값은 " + answer + "입니다") 

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일때는 +로 표시, 음수일때는 -로 표시 
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(-500))
# 3자리마다 콤마 찍어주기
print("{0:,}".format(100000000000))
# 3자리마다 콤마 찍어주기, +-부호도 붙이기
print("{0:+,)",format(10000000000))
print("{0:+,)",format(-10000000000))
# 3자리마다 콤마 찍어주기, 부호 붙이고 자릿수 확보, 빈자리는 ^채우기
print("{0:^<+30,}".format(100000000000))
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 측정 자리수까지만 표시 (소수점 3째 자리에서 반올림)
print("{0:.2f}".format(5/3))


# 파일입출력
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학: 80")
score_file.write("\n코딩: 100") # 줄바꿈
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄별로 읽기, 한줄읽고 커서는 다음줄로 
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close() 

score_file = open("score.txt", "r", encoding="utf8")
while True: 
    line = score_file.read()
    if not line: 
        break 
    print(line, end="")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end="")
score_file.close()


# pickle 
import pickle
profile_file = open("profile.pickle", "wb") # 피클은 바이너리 타입 정의 반드시, 인코딩 필요없음
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)
pickle.dump(profile, profile_file)
profile_file.close() 

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기 
print(profile)
profile_file.close()

# with 
import pickle 

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

# Q7. 당신의 회사에서는 매주 1회 작성해야 하는 보고서가 있습니다.
# 보고서는 항상 아래와 같은 형태로 출력되어야 합니다.
# -  x 주차 주간보고 - 
# 부서 :
# 이름 :
# 업무 요약: 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오
# 조건: 파일명은 '1주차. txt', '2주차. txt', ...와 같이 만듭니다. 

for i in range(1, 51):
    with open(str(i)+ "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고".format(i))
        report_file.write("\n부서 :")
        report_file.write("\n이름 :")
        report_file.write("\n업무 요약: ")




# 클래스 (스타크래프트)
from random import * 
# 마린 : 공격유닛, 군인, 총을 쏠 수 있음
name = "마린" 
hp = 40
damage = 5 
print("{} 유닛이 생성되었습니다".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 ; 공격유닛, 탱크, 포를 쏠 수 있고 일반/시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합ㄴ다. [공격력 {2}".래금ㅅ( \
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)

# 일반유닛 
class Unit: # class 복사, 객체 생성 self 제외하고 모두 넣어주어야 
    def __init__(self, name, hp, speed):  # __ 생성자 
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0}유닛이 생성되었습니다".format(name))

    def move(self, location):
        print("[지상유닛 이동]")
        print("{0}:{1}방향으로 이동합니다 [속도 {2}"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0}:{1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0}:현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0}: 파괴되었습니다.".format(self.name))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# # 레이스 : 공중유닛, 비행기, 클로킹(스탤스)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # .으로 

# # 마인드컨트롤 : 상대방 유닛을 내 것으로 만드는것 
# wraith2 = Unit("레이스", 80, 5)
# wraith2.clocking = True # clocking 외부 변수 추가 할당

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다".format(wraith2.name))

# 공격유닛 
class AttackUnit(Unit): # 일반유닛 부모클래스 Unit 상속, 성격 물려받음  
        def __init__(self, name, hp, speed, damage):  # __ 생성자 
            Unit.__init__(self, name, hp, speed) # name과 hp 상속 
            self.damage = damage # damage만 추가 

        def attack(self, location):
            print("{0}:{1} 방향으로 적군을 공격합니다. [공격력 {2}"\
                .format(self.name, location, self.damage))

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩: 일정 시간 공격 이동/속도 증가, 자기체력 10 감소 
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0}: 스팀팩을 사용합니다. (HP 10감소)".format(self.name))
        else:
            print("{0}: 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# 탱크
class Tank(AttackUnit):
    # 시즈모드: 탱크를 지상에 고정, 더 높은 파워 공격, 이동불가
    seize_developed = False # 시즈모드 개바ㅏㄹ여부
    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False 
   
    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
    # 시즈모드가 아닐 때 -> 시즈모드 
        if self.seize_mode == False:
            print("{0}: 시즈모드로 전환합니다".format(self.name))
            self.damage *= 2 
            self.seize_mode = True 

    # 시즈모드일때 -> 해제  
        else:
            print("{0}: 시즈모드를 해제합니다".format(self.name))
            self.damage /= 2 
            self.seize_mode = False 

# 파이어뱃: 공격유닛, 화염방사기
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 드랍쉽 : 공중유닛, 수송기, 공격기능 없음 
class Flyable: # 날수 있는 기능 가진 클래스  
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed 

    def fly(self, name, location):
        print("{0}:{1} 방향으로 날아갑니다. [속도 {2}"\
            .format(name, location, self.flying_speed))

# 공중공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 다중상속, 클래스 두개 상속 
    def __init__(self, name, hp, damage, flying_speed): 
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상스피드는 0 
        Flyable.__init__(self, flying_speed)

    def move(self, location):  # 메소드 오버라이딩 
        self.fly(self.name, location) 

# 발키리: 공중공격유닛, 한번에 14발 미사일 발사 
valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시")


# 벌처 : 지상유닛, 기동성이 좋음
vulture = AttackUnit("벌처", 80, 10, 20)
# 배틀크루저 : 공중유닛, 체력좋음, 공격력 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시") 


# pass
# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
       # Unit.__init__(self, name, hp, 0)
        super().__init__(name, hp, 0) # self 없음 
        self.location = location 

# 레이스
class Wraith(FlyableAttackUnit): 
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False # 클로킹 해제 상태
    
    def clocking(self):
        if self.clocked == True: # 클로킹모드 -> 해제 
            print("{0}: 클로킹모드 해제 합니다".format(self.name))
            self.clocked = False
        else:    # 클로킹 해제 -> 모드 설정        
            print("{0}: 클로킹모드 설정 합니다".format(self.name))
            self.clocked = True 

def game_start():
    print("[알림] 새로운 게임을 시작합니다")
def game_over():
    print("Player : GG")
    print("[Player]님이 게임에서 퇴장하셨습니다")


# 게임 시작 
game_start()

# 마린 3기 생성 
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 ㅅ애성
w1 = Wraith()

# 유닛 일괄 관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_developed = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다")

# 공격 모드 준비 (마린: 스팀팩, 탱크: 시즈모드, 레이스: 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine): # ~의 경우 
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격 
for unit in attack_units:
    unit.attack("1시")

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5, 21)) # 공격 랜덤으로 받음 5~20 

# 게임 종료
game_over() 