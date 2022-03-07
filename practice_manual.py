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

print(abs(-5)) #5 절대값
print(pow(4, 2)) #4^2 제곱
print(max(5, 12)) #12 최대값
print(min(5, 12)) #5 최소값 
print(round(3.14)) #3 반올림 


animal = "고양이"
name = "해피"
age = 4
hobby = "낮잠"
is_adult = age >= 3

print("우리집" + animal + "의 이름은" + name + "예요")
hobby = "공놀이"
print(name,"는 ", age, "살이며", hobby, "을 아주 좋아해요")
print(name+ "는 어른일까요?" + str(is_adult))
