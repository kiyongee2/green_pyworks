import sys

x = input("수 입력 : ")
n = int(x)

if n == 0:
    print("0으로 나눌 수 없습니다.")
    sys.exit(0)

result = 10 / n

print(result)

"""
try:
    x = input("수 입력 : ")
    n = int(x)

    result = 10 / n

    print(result)
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
"""