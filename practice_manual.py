# 초기 설정을 구현합니다  
# Git Bash 실행 
    # git config --global user.name 이름
    # git config --global user.email 이메일 주소
# VSCode 실행
    # New File 생성 
    # 파일명은 practice_닉네임.py 
    # 적당한 폴더에 저장 <- 앞으로 변경하지 않습니다 
    # git init 
    # git remote add origin https://github.com/yr-x/learninglab1.git
    # git add 파일명 또는 git add .
    # git commit -m "제출합니다" 
    # git branch -M main 
    # git push -u origin main 


# 학습을 시작합니다 
print("hello world") #hello world

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

animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집" + animal + "의 이름은" + name + "예요")
hobby = "공놀이"
print(name,"는 ", age, "살이며", hobby, "을 아주 좋아해요")
print(name+ "는 어른일까요?" + str(is_adult))


print(abs(-5)) #5 절대값
print(pow(4, 2)) #4^2 제곱
print(max(5, 12)) #12 최대값
print(min(5, 12)) #5 최소값 
print(round(3.14)) #3 반올림 
print(round(4.99)) #5

from ipaddress import NetmaskValueError
from math import *
print(floor(4.99)) #내림 4
print(ceil(3.14)) #올림 4
print(sqrt(16)) #제곱근 4

from random import *
print(random()) #0~1 임의값
print(random() * 10) # 0~10
print(int(random() * 10)) # 0~10 정수 임의값
print(int(random() * 10) + 1) #1~10 정수 임의값 
print(randrange(1, 26)) #1~45 정수 임의값 
print(randint(1, 45)) #1~45 정수 임의값 

# Q. 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다. 
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
print ("C:\Users\2920513\Hyundai Motor and Kia\My Document\PythonWorkbook\practice_manual.py") # \\문장 내에서 \
print("Red Apple\rPine") # \r 커서를 맨앞으로 이동 
print("Redd\bApple") # \b 백스페이스 한글자 삭제 
print("Red\tApple") # \t 탭

# # Q 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
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
#모두 지우기
num_list.clear()
print(num_list)
# 다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)
# 리스트 확장
num_list.extend(mix_list)
print(num_list)

# 사전


