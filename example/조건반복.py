# 나누기
"""
bread = 30
people = 4

나누기 = bread / people
몫 = bread // people
몫2 = int(bread / people)
나머지 = bread % people

print(나누기)
print(몫)
print(몫2)
print(나머지)
"""

# input() 함수
"""
print("문자 입력: ")
ch = input()
print(ch)

num = input("숫자 입력: ")
num = int(num)
print(num + 5)
"""

# 나이 계산 프로그램
"""
current_year = 2023
birth_year =input("태어난 년도를 입력하세요: ")
age = current_year - int(birth_year) + 1
print(age)
"""

# 놀이 공원 입장료 계산
"""
age = int(input("나이 입력: "))
charge = 0

if age < 8:
    print("취학전 아동입니다.")
    charge = 1000
elif age >= 8 and age < 14:
    print("초등학생입니다.")
    charge = 2000
elif age >= 14 and age < 20:
    print("중,고등학생입니다.")
    charge = 2500
else:
    print("성인입니다..")
    charge = 3000

print("입장료는 " + str(charge) + "원입니다." )
"""


# 자리배치도 프로그램
"""
customer = int(input("입장객 수: "))  
col_num = int(input("좌석 열 수: "))
row_num = 0  #좌석 줄 수

if customer % col_num == 0:
    row_num = int(customer / col_num)
else:
    row_num = int(customer / col_num) + 1
print(str(row_num) + "개의 줄이 필요합니다.")
"""
    
# 윤년을 계산하는 프로그램
"""
year = int(input("연도를 입력하세요: "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(f"{year}년은 윤년입니다.")
else:
    print(f'{year}년은 평년입니다.')
"""
    
# 교통 수단 이용하기
"""
money = 3000
card = False

if money >= 4000 or card:
    print("택시를 탄다")
elif money >= 2000 or not card:
    print("버스를 탄다")
else:
    print("걸어간다.")

print('=' * 30)

pocket = ['paper', '스마트폰', 'money']

if 'coin' in pocket:
    print("택시를 탄다")
else:
    print("지하철을 탄다.")
"""

# 체질량 지수 BMI 계산하기
# bmi = 몸무게 / 키 ** 2(키의 제곱)
"""
name = input("이름을 입력하세요: ")
height = float(input("키를 입력하세요: "))
height = height / 100  # m -> cm로 환산
weight = float(input("몸무게를 입력하세요: "))

bmi = weight / (height ** 2)
print("%s님의 bmi는 %.1f입니다." % (name, bmi))

if bmi < 20:
    print("저체중입니다.")
elif bmi >= 20 and bmi < 25:
    print("정상입니다.")
elif bmi >= 25 and bmi < 30:
    print("과체중입니다.")
else:
    print("비만입니다.")
"""

# 1부터 10까지 합계
"""
i = 0
sum_v = 0

while i < 10:
    i = i + 1   # 1증가
    sum_v += i  # 누적합계
    print("i=",i, "sum_v=", sum_v)
    
print("합계는", sum_v)

# while ~ break문
i = 0

while True:
    i += 1
    if i > 10:
        break
    print(i)
"""
# 반복 조건문
"""
while True:
    answer = input("반복을 계속 할까요?(y/n)")
    if answer == 'y' or answer == 'Y':
        print("반복을 계속합니다.")
    elif answer == 'n' or answer == 'N':
        print("반복을 중단합니다.")
        break
    else:
        print("정상 답변이 아닙니다.")
"""

"""
# 커피 자동판매기 프로그램
coffee = 5

while True:
    coin = int(input("돈을 넣어주세요: "))
    
    if coin == 400:
        print("커피가 나옵니다.")
        coffee = coffee - 1
    elif coin > 400:
        print("커피가 나오고, 거스름돈", coin-400, "원을 돌려 받습니다.")
        coffee = coffee - 1
    else:
        print("커피가 나오지 않습니다.")
    print("남은 커피의 양은", coffee, "개입니다.")
    
    if coffee == 0:
        print("커피가 모두 소진되었습니다. 판매를 중지합니다.")
        break

"""

# 1부터 10까지 합계
"""
for i in range(1, 11, 2):
    print(i, end=' ')

for i in range(1, 11):
    if i % 2 == 1:
        print(i, end=' ')

sum_v = 0
for i in range(1, 11):
    sum_v = sum_v + i
print(sum_v)

sum_v2 = 0
for i in range(1, 11):
    if i % 2 == 0:
        sum_v2 = sum_v2 + i
print("짝수 합계:", sum_v2)

# 구구단
dan = int(input("단을 입력하세요: "))
for i in range(1, 10):
    print(f'{dan} x {i} = {dan*i}')
"""

# 중첩 for
"""
for i in range(5):
    for j in range(5):
        print('$', end='')
    print()
print('='*30)
for i in range(0, 5):
    for j in range(0, i+1):
        print('*', end='')
    print()
print('='*30)

for i in range(0, 5):
    for j in range(0, 5-i):
        print('*', end='')
    print()
print('='*30)

for i in range(0, 5):
    for j in range(1, 6):
        print(5*i+j, end=' ')
    print()
print('='*30)
"""

# 구구단(전체)
"""
for i in range(2, 10):
    print('[', i, '단]')
    for j in range(1, 10):
        print(f"{i} * {j} = {i*j}")
print('='*30)

for i in range(1, 10):
    for j in range(2, 10):
        print(f"{j} * {i} = {j*i}", end=' | ')
    print()
print('='*30)
"""
"""
start_dan = int(input("시작단 입력: "))
end_dan = int(input("끝단 입력: "))

result_val = ''
for i in range(start_dan, end_dan+1):
    for j in range(1, 10):
        #current_val = '{}x{}={}\n'.format(i, j, i*j)
        current_val = f'{i} x {j} = {i * j}\n'
        result_val = result_val + current_val
print(result_val)

style = input("단을 구분할 줄 모양 입력: ")

result_val = ''
for i in range(2, 10):
    for j in range(1, 10):
        current_val = f'{i} x {j} = {i * j}\n'
        result_val = result_val + current_val
    if i <= 9:
        result_val = result_val + style + '\n'
print(result_val)
"""
    
# 자리배치도 프로그램(완성)
"""
print("*** 자리배치도 ***")

customer = int(input("입장객 수: "))  
col_num = int(input("좌석 열 수: "))
row_num = 0  #좌석 줄 수

if customer % col_num == 0:
    row_num = customer / col_num
else:
    row_num = int(customer / col_num) + 1
#print(str(row_num) + "개의 줄이 필요합니다.")


for i in range(0, row_num):
    for j in range(1, col_num+1):
        seat_num = col_num*i+j
        if seat_num > customer:
           break 
        print(seat_num, end=' ')
    print()
"""
    

















