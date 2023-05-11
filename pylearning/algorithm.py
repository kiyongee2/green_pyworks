# 최대, 최소



# 오름차순 정렬
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
a        60 5 33 12 97 24
i=0(1행)  5 33 12 60 24 97 
i=1(2행)  5 12 33 24 60 97
i=2(3행)  5 12 24 33 60 97  
'''

# 랭크


# 동명이인 - 중복값 찾기
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
