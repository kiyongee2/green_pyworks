import random
import sys

print("♠ 가위 바위 보 게임 ♠")
가위바위보 = ['가위', '바위', '보']

you = input('당신 : ')

# random.choice() 사용
com = random.choice(가위바위보)
print("컴퓨터 :", com)

# random.randint() 사용
# rnd = random.randint(0, 2)
# com = 가위바위보[rnd]
# print("컴퓨터 :", com)

if you not in 가위바위보:
    print("잘못된 입력입니다. 다시 입력해주세요")
    sys.exit(0)

if you == com:
    print('결과 : 무승부')
elif you == '가위' and com == '보':
    print("결과 : 승")
elif you == '바위' and com == '가위':
    print("결과 : 승")
elif you == '보' and com == '바위':
    print("결과 : 승")
else:
    print("결과 : 패")




