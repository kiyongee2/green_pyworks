# 구구단
"""
def gugudan(dan):
    for i in range(1, 10):
        print(dan, "x", i, '=', dan * i)

gugudan(5)
"""

# 주문 상품 가격이 20,000원 미만이면 배송비(2,500원) 포함
# 변수 - price, quantity, fee, unit_price
"""
def get_price(unit_price, quantity):
    price = unit_price * quantity  # 가격 = 단위가격 x 수량
    fee = 2500
    if price < 20000:
        return price + fee
    else:
        return price

price1 = get_price(15000, 2)
price2 = get_price(5000, 3)

print("가격 1: " + str(price1) + "원")
print("가격 2: " + str(price2) + "원")
"""

# 두 수를 매개 변수로 전달하여 서로 같으면 곱하고,
# 서로 다르면 더하는 함수 정의
"""
def func(x, y):
    if x == y:
        return x * y
    else:
        return x + y

num1 = func(10, 20)
num2 = func(10, 10)
print("num1 =", num1)
print("num2 =", num2)
"""

# 1부터 10까지 더하기
def sum_n(n):
    sum_v = 0
    for i in range(1, n+1):
        sum_v += i
    return sum_v

def sum_n2(n):
    sum_v = (n * (n + 1)) // 2
    return sum_v

print(sum_n(10))
print(sum_n2(10))

# 리스트를 매개변수로 전달하여 평균 계산하기
"""
def get_average(a):
    sum_v = 0
    for i in a:
        sum_v += i
    return sum_v /len(a)

v = [1, 2, 3, 4]
print(f'평균: {get_average(v)}')
"""

# 최대값과 최대값의 위치 구하기
# 최대값 정의
"""
def find_max(a):
    max_v = a[0]
    for i in a:
        if max_v < i:
            max_v = i
    return max_v

# 최대값 위치 정의
def find_max_idx(a):
    max_idx = 0
    for i in range(len(a)):
        if a[max_idx] < a[i]:
            max_idx = i

    return max_idx

v = [70, 80, 55, 60, 90, 40]
max_value = find_max(v)
max_index = find_max_idx(v)

print("최대값:", max_value)
print("최대값의 위치:", max_index)
"""

# 리스트를 매개 변수로 새로운 리스트 만들기
"""
def times(a):
    a2 = []
    for i in a:
        a2.append(3*i)
    return a2

v = [1, 2, 3, 4]
v2 = times(v)
print(v2)
"""

# 동명이인 찾기
def find_same_name(a):
    same_name = set()
    n = len(a)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] == a[j]:
                same_name.add(a[i])
    return same_name
    """
    i=0, j=1, a[0] == a[1]
         j=2, a[0] == a[2]  
         j=3, a[0] == a[3]
    i=1, j=2, a[1] == a[2]  
         j=3, a[1] == a[3] '을지문덕'
    i=2, j=3, a[2] == a[3]
         
    """ 
name = ['이순신', '을지문덕', '강감찬', '이순신']
print(find_same_name(name))

# 전역 변수
"""
def one_up():
    global x
    x += 1
    return x

x = 1
print(one_up())
print(one_up())
print(one_up())
"""

# 30까지의 배수와 개수
"""
def times(x):
    global count
    for i in range(1, 31):
        if i % x == 0:
            count += 1
            print(i, end=' ')

count = 0
times(4)
print(f'\n배수의 개수 : {count}')
"""

# 내장 함수
"""
print(abs(-3))
print(round(3.67))
print(pow(2, 4))

def my_pow(x, y):
    num = 1
    for i in range(0, y):
        num = num * x
    return num

    # i=0, num = 1*2
    # i=1, num = (2)*2
    # i=2, num = (2)*2*2
    # i=3, num = (2)*2*2*2

print(my_pow(2, 4))
"""











