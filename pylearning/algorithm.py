# 최대, 최소



# 오름차순 정렬
"""
a = [60, 5, 33, 12, 97, 24]

#1. 내장 함수 sort()
a.sort() # 오름차순 정렬
print(a)
a.sort(reverse=True) #내림 차순
print(a)

#2. 반복 조건문 - 정렬 알고리즘
n = len(a)
for i in range(0, n):
    for j in range(0, n-1):
        if a[j] > a[j+1]:
            #교환
            a[j], a[j+1] = a[j+1], a[j]
            '''
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            '''
print(a)
'''
i=0 j=0 a[0]>a[1] True 5, 60, 33, 12, 97, 24
    j=1 a[1]>a[2] True 5, 33, 60, 12, 97, 24
    j=2 a[2]>a[3] True 5, 33, 12, 60, 97, 24
    j=3 a[3]>a[4] False 5, 33, 12, 60, 97, 24
    j=4 a[4]>a[5] True 5, 33, 12, 60, 24, 97
i=1 j=0 a[0]>a[1] False 5, 33, 12, 60, 24, 97
    j=1 a[1]>a[2] True 5, 12, 33, 60, 24, 97
    j=2 a[2]>a[3] False 5, 12, 33, 60, 24, 97
    j=3 a[3]>a[4] True 5, 12, 33, 24, 60, 97
    j=4 a[4]>a[5] True 5, 12, 33, 24, 60, 97
i=2 j=0 a[0]>a[1] False 5, 12, 33, 24, 60, 97
    j=1 a[1]>a[2] False 5, 12, 33, 24, 60, 97
    j=2 a[2]>a[3] True 5, 12, 24, 33, 60, 97 (정렬끝)
'''
"""

# 랭킹(ranking)
score = [60, 5, 33, 12, 97, 24]
rank = [1, 1, 1, 1, 1, 1]  # 순위를 모두 1로 설정
n = len(score)

for i in range(0, n):
    for j in range(0, n):
        if score[i] < score[j]:
            rank[i] = rank[i] + 1  # 순위 1증가

print(rank)
'''                              
i=0 j=0 score[0] < score[0] False  rank[0] 1
    j=1 score[0] < score[1] False  rank[0] 1
    j=2 score[0] < score[2] False  rank[0] 1
    j=3 score[0] < score[3] False  rank[0] 1
    j=4 score[0] < score[4] True   rank[0] 2
    j=5 score[0] < score[5] False  rank[0] 2(순위 확정)
i=1 j=0 score[1] < score[0] True  rank[1] 2
    j=1 score[1] < score[1] False  rank[1] 2
    j=2 score[1] < score[2] True  rank[1] 3
    j=3 score[1] < score[3] True  rank[1] 4
    j=4 score[1] < score[4] True  rank[1] 5
    j=5 score[1] < score[5] True  rank[1] 6(순위 확정)
i=2 j=0 score[2] < score[0] True  rank[2] 2
    j=1 score[2] < score[1] False  rank[2] 2
    j=2 score[2] < score[2] False  rank[2] 2
    j=3 score[2] < score[3] False  rank[2] 2
    j=4 score[2] < score[4] True  rank[2] 3
    j=5 score[2] < score[5] False  rank[2] 3(순위 확정)
'''

# 동명이인 - 중복값 찾기
"""
name = ['흥부', '콩쥐', '놀부', '콩쥐']
same_name = set()  # 빈 집합 생성
print(same_name)
n = len(name)
for i in range(0, n-1):
    for j in range(i+1, n):
        if name[i] == name[j]:
            # 중복이름 추가
            same_name.add(name[i])
'''
i=0 j=1 name[0] == name[1]  '흥부'=='콩쥐'
    j=2 name[0] == name[2]  '흥부'=='놀부'
    j=3 name[0] == name[3]  '흥부'=='콩쥐'
i=1 j=2 name[1] == name[2]  '콩쥐'=='놀부'
    j=3 name[1] == name[3]  '콩쥐'=='콩쥐'  중복찾음
i=2 j=3 name[2] == name[3]  '놀부'=='콩쥐'
'''
print(same_name)
"""

# 순차 탐색
# 특정 값을 찾아서 해당 위치 번호를 돌려줌
def search_list(a, x):
    n = len(a)
    for i in range(0, n): # 모든 값을 차례로
        if x == a[i]:     # x값과 비교하여 같으면
            return i      # 위치를 돌려줌
    return -1

v = [60, 5, 33, 12, 97, 24, 12]

print(search_list(v, 5))
print(search_list(v, 12))
print(search_list(v, 111))

def search_list2(a, x):
    same_num = []
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            same_num.append(i)
    return same_num or -1

print(search_list2(v, 5))
print(search_list2(v, 12))
print(search_list(v, 111))


n = len(v)
for i in range(0, n):
    if 12 == v[i]:
        print("찾음")


# 연습 문제
# 학생 번호를 입력하면 학생 번호에 해당하는 이름을 순차 탐색으로
# 찾아 돌려주는 함수 만들기
def search_list(a, x):
    n = len(a)
    for i in range(0, n):
        if x == a[i]:
            return name[i]

    return '?'

v = [60, 5, 33, 12, 97, 24]

name = ['이순신', '강감찬', '서희', '안중근', '유관순', '이율곡']

print(search_list(v, 5))
print(search_list(v, 12))
print(search_list(v, 111))

# 이분 탐색
# 리스트에서 특정 숫자 찾기
'''
def binary_search(a, x):
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            start = mid + 1
        else:
            end = mid - 1

d = [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(binary_search(d, 36))
print(binary_search(d, 50))
'''
'''
1차 검색
mid = 4 d[4] = 25 36 > 25 찾지 못함
start = 36 end = 81 찾음.

'''