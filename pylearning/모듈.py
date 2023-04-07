# 내장 모듈
import datetime
import calendar
import time
import random

# datetime 모듈
"""
now = datetime.datetime.today()
#now = datetime.date.today()
print(now)
print(now.strftime('%Y. %m. %d. %H:%M:%S'))

print(f'{now.year}년')
print(f'{now.month}월')
print(f'{now.day}일')

age = int(input("나이 입력 : "))

result = now.year + (100 - age)
print(f'100세 되는 해는 {result}년 입니다.')

print("지금까지 몇 일?")
dday = datetime.date(2023, 5, 5)
print(dday)
today = datetime.date.today()

passedtime = dday - today
print(f'Dday : {passedtime.days}일')
"""

# calendar 모듈
"""
#calendar.prcal(2023)
#calendar.prmonth(2023, 4)
print(calendar.weekday(2023, 4, 1))

days = ['월', '화', '수', '목', '금', '토', '일']

weekday = datetime.date(2023, 4, 7).weekday()
print(weekday)
print(days[weekday])

def get_weekday(yyyy, mm, dd):
    days = ['월', '화', '수', '목', '금', '토', '일']
    idx = datetime.date(yyyy, mm, dd).weekday()
    print("{}년 {}월 {}일 {}요일".format(yyyy, mm, dd, days[idx]))

get_weekday(2023, 4, 5)
"""

# time 모듈
"""
print(time.time())
print(time.localtime())
print(time.ctime())

year = round(time.time()/(365*24*60*60), 1)
day = round(time.time()/(24*60*60))
print(f'{year}년')
print(f'{day}일')
"""

# 수행 시간 측정
"""
start = time.time()

for i in range(1, 11):
    print(i)
    time.sleep(1)
    
end = time.time()
print(f'수행시간 : {end-start}초')
"""

# 속으로 20초를 세어 맞히는 프로그램
"""
input("엔터를 누르고 20초를 셉니다.")
start = time.time()

input("20초 후에 다시 엔터를 누릅니다.")
end = time.time()

et = end - start
print(f'실제 시간 : {et:.2f}초')
"""

# up and down 게임
"""
com = random.randint(1, 100)
print(com)
min_v = 1
max_v = 100
for i in range(10):
    try:
        guess = int(input(f'맞혀보세요([{i+1}회] {min_v} ~ {max_v})? '))
        if guess == com:
            print("정답!")
            break
        elif guess > com:
            print("너무 커요")
            max_v = guess
        else:
            print("너무 작아요")
            min_v = guess
    except ValueError:
        print("숫자로 입력해 주세요.")

print(f'정답 : {guess}')
print(f'점수 : {(10 - i) * 10}점')
"""

# lotto 복권
lotto = []
"""
# 중복된 경우 5개만 저장됨
for i in range(6):
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)
"""
while len(lotto) < 6:
    print(len(lotto))
    n = random.randint(1, 45)
    if n not in lotto:
        lotto.append(n)

print(lotto)

# random 모듈
"""
days = ['월', '화', '수', '목', '금', '토', '일']
print(random.choice(days))

print(random.randint(1, 10))

dice = random.randint(1, 6)
print(dice)

for x in range(1, 11):
    dice = random.randint(1, 6)
    print(dice, end=' ')

for i in range(10):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    print(total)
    if total == 7:
        print("Seven Thrown!!")
    if total == 11:
        print("Eleven Thrown!!")
    if dice1 == dice2:
        print("Double Thrown!!")
"""

# 모듈(클래스) 사용하기
"""
from my_module import Student

# 인스턴스 2개 생성
s1 = Student("이순신", 1)
print(s1)
s1.learn()

s2 = Student("권율", 3)
print(s2)
s2.learn()
"""

# 객체 배열(리스트) 생성
"""
student = [
    Student("김하나", 1),
    Student("이둘", 2),
    Student("박셋", 3)
]

print("***** 학생 명단 *****")
for s in student:
    print(s)
"""
