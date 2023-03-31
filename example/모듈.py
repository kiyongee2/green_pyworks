# 내장 모듈
import datetime
import calendar
import random

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

#calendar.prcal(2023)
#calendar.prmonth(2023, 4)
print(calendar.weekday(2023, 4, 1))

days = ['월', '화', '수', '목', '금', '토', '일']

weekday = datetime.datetime(2023, 4, 1).weekday()
print(weekday)
print(days[weekday])
"""
days = ['월', '화', '수', '목', '금', '토', '일']
print(random.choice(days))

print(random.randint(1, 10))

dice = random.randint(1, 6)
print(dice)

for x in range(1, 11):
    dice = random.randint(1, 6)
    print(dice, end=' ')

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

# 객체 배열(리스트) 생성
student = [
    Student("김하나", 1),
    Student("이둘", 2),
    Student("박셋", 3)
]

print("***** 학생 명단 *****")
for s in student:
    print(s)
"""
