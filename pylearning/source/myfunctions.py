# 거듭제곱 구하기
def mypow(x, y):
    num = 1
    for i in range(0, y):
        num = num * x
    return num
# 문자 반복 출력
def print_string(text, count=1):
    for i in range(count):
        print(text)

if __name__=="__main__":
    # 거듭제곱 함수 호출
    print(mypow(2, 4))
    print(mypow(10, 3))
    print(pow(2, 4))  #내장 함수

    # 기본 매개변수 함수 호출
    print_string('새벽')
    print_string('새벽', 3)

