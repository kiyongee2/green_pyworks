# 가변 매개 변수
def get_avg(*number):
    sum_v = 0
    for i in number:
        sum_v += i
    avg = sum_v / len(number)
    return avg

def merge_text(*text):
    result = ""
    for txt in text:
        result += txt
    return result

val1 = get_avg(1, 2, 3)
print(val1)

str1 = merge_text('치약', '칫솔')
str2 = merge_text('치약', '칫솔', '수건')
print(str1)
print(str2)

# 딕셔너리형 자료
def print_kw(**kwargs):
    print(kwargs)

print_kw(name='진')
print_kw(name='진', age=32)

# 재귀 함수
# 1부터 10까지 곱하기
"""
def facto(n):
    if n <= 1:
        return 1
    else:
        return n * facto(n-1)

print(facto(1))
print(facto(2))
print(facto(3))
"""
# sos - "Help me" 반복하기
"""
def sos(i):
    print("Help me")
    if i == 1:
        return ""
    else:
        return sos(i - 1)

sos(3)
sos(1)
"""

# 피보나치 수열
# 1 1 2 3 5 8...
"""
def fibo(n):
    if n <= 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
    
    n=1항 fibo(1)  1
    n=2   fibo(2)  1
    n=3   fibo(1) + fibo(2) 1+1=2
    n=4   fibo(2) + fibo(3) 1+2=3

print(fibo(1))
print(fibo(2))
print(fibo(3))
"""


# 람다 함수
"""
one_up = lambda x : x + 1
print(one_up(1))

print((lambda x : x + 1)(2))

add = lambda x, y : x + y
print(add(3, 4))
print((lambda x, y : x + y)(3, 4))

print("콜백(callback) 함수")
def call_10(func):
    for i in range(10):
        func()

hello = lambda : print("안녕하세요")
call_10(hello)

#(lambda s : print(s))('hello')

"""
def times(a):
    a2 = []
    for i in a:
        a2.append(3 * i)
    return a2

v = [1, 2, 3, 4]
print(times(v))

times2 = lambda x : 3 * x
result = map(times2, v)
print(list(result)) #result 객체를 리스트로 변환

# 시간 복잡도 계산하기
# 1부터 10까지 더하기
import time
start = time.time()
def sum_n(n):
    sum_v = 0
    for i in range(1, n+1):
        sum_v += i
    return sum_v

def sum_n2(n):
    sum_v = (n * (n + 1)) // 2
    return sum_v

print(sum_n(10000000))
#print(sum_n2(10000000))
end = time.time()
print(f"소요 시간 : {(end-start)}초")
