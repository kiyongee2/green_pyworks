import sys

"""
#print(sys.argv)
print(sys.argv[1:]) # 1번 인덱스부터 출력

"""

args = sys.argv[1:]
print(args)

total = 0
for i in args:
    total += int(i) #문자형을 숫자로 변환

print(total)

