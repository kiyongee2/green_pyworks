# 리스트(배열)
"""
season = ['봄', '여름', '가을', '겨울']

print(season[0])
print(season[-1])

print(season)

for i in season:
    print(i)

print(season[1:3])
print(season[:4])
print(season[:])
print(season[:-1])
"""

# 리스트 수정, 삭제
"""
score = [90, 80, 50, 100]

score[2] = 70
print(score)

del score[1]
print(score)
"""

# 리스트 주요 함수(메서드)
"""
# 리스트의 요소 추가
a = [1, 2, 3]
a.append(4)
print(a)

a.insert(1, 5)
print(a)

# 리스트 요소 삭제
a.pop()
print(a)

car = ['모닝', 'BMW', '벤츠', '스포티지']
car.remove('BMW')
print(car)
print(len(car))
"""

# for 변수 in 리스트
"""
number = [12, 99, 25, 73, 50]
print(99 in number)
print(24 in number)
print()

for n in number:
    print(n, end=' ')
print()

for n in number:
    if n < 50:
        print(n)

print()
languages = ['python', 'C', 'Java', 'Javascript']

for lang in languages:
    if lang in ['python', 'Javascript']:
        print("%s need interpreter" % lang)
    elif lang in ['C', 'Java']:
        print("%s need compiler" % lang)
"""

# 리스트의 연산
"""
score = [70, 80, 50, 60, 90, 40]
sum_v = 0
count = len(score)
for i in score:
    sum_v += i

avg = sum_v / count

print("개수:", count)
print("합계:", sum_v)
print("평균:", avg)

# 내장함수 sum()
print("합계:", sum(score))
"""

# 최고 점수, 최저 점수
"""
max_v = score[0]
min_v = score[0]

for i in score:
    if max_v < i:
        max_v = i

# for ~ range()
for i in range(count):
    if max_v < score[i]:
        max_v = score[i]

for i in score:
    if min_v > i:
        min_v = i

print("최고 점수:", max_v)
print("최고 점수:", max(score))
print("최저 점수:", min_v)
print("최저 점수:", min(score))

# 최고 점수, 최저 점수 위치 찾기
max_idx = 0
min_idx = 0
for i in range(count):
    if score[max_idx] < score[i]:
        max_idx = i

for i in range(count):
    if score[min_idx] > score[i]:
        min_idx = i
        
print("최고 점수 위치:", max_idx)
print("최고 점수 위치:", min_idx)
"""

# 리스트 복사
"""
d = [1, 2, 3, 4]
d2 = []
print("d =", d)

for i in d:
    d2.append(i)

print("d2 =", d2)

# 3의 배수로 저장
d3 = []
for i in d:
    d3.append(i * 3)
print("d3 =", d3)

dd3 = [ i * 3 for i in d]
print("dd3 =", dd3)


# 홀수만 복사하기
d4 = []
for i in d:
    if i % 2 == 1:
        d4.append(i)
print("d4 =", d4)

dd4 = [i for i in d if i % 2 == 1] 
print("dd4 =", dd4)
"""

# 2차원 리스트의 선언 및 생성
"""
d = [
    [10, 20],
    [30, 40],
    [50, 60]
]
print(d[0][0])
print(d[0][1])
print(d[1][0])
print(d[1][1])

for x, y in d:
    print(x, y)

print(len(d))
print(len(d[0]))

for i in range(len(d)):
    for j in range(len(d[i])):
        print(d[i][j])
    print()

# 요소 추가
d.append([70, 80])
print(d)

# 2차원 리스트의 연산
sum_v = 0
count = 0
avg = 0.0

for i in range(len(d)):
    for j in range(len(d[i])):
        count += 1
        sum_v += d[i][j]
avg = sum_v / count

print("합계:", sum_v)
print("개수:", count)
print("평균:", avg)

# 성적 통계

"""

# 튜플
"""
t1 = (1, )
t2 = (2, 3, 4)

print(t1 + t2)

print(t2[-1])

# t2[0] = 5
#del t2[1]

# set
s = {2, 4, 6, 8}
print(s)

# set() 함수 - 중복을 허용하지 않고, 순서 없음
say = set('hello')
print(say)

s.add(10)  # 요소 추가
print(s)

s.remove(4) # 요소 삭제
print(s)

s2 = set()  # 빈 집합
print(s2)
s2.add(1)
print(s2)

a = [1, 1, 1, 2, 3, 3]
set_v = set(a)

print(set_v)
print(list(set_v))

# 합집합, 교집합, 차집합
"""

# 딕셔너리
"""
p = {}
print(p)

# 요소 추가
p['name'] = "오상식"
p['age'] = 35
print(p)
p['phone'] = "010-1234-5678"

# 특정 요소 출력
print(p['name'])

# 요소 삭제
del p['age']
print(p)

# 전체 출력
for key in p:
    print(key, ':', p[key])


d = {'Tomas': 13, 'Jane': 9}
d['Mike'] = 10
print(d)

del d['Jane']  # 요소 삭제

print(d.keys())
print(d.values())
print(d.items())

for key, val in d.items():
    print(key, val)
"""

# 학생의 성적 통계
"""
student = [
    {"name":"이대한", "kor":80, "eng":80, "math":75},
    {"name":"박민국", "kor":70, "eng":65, "math":60},
    {"name":"오상식", "kor":75, "eng":70, "math":50},
    {"name":"최지능", "kor":70, "eng":90, "math":90}

]
print(" 이름  국어 영어 수학")
for std in student:
    print("%s  %d   %d   %d"  % (std["name"], std["kor"], std["eng"], std["math"]))

print("="*30)

# 개인별 총점과 평균
print(" 이름   총점  평균")
for std in student:
    total = std["kor"] + std["eng"] + std["math"]
    avg = total / 3
    print("%s  %d   %.1f"  % (std["name"], total, avg))

# 과목별 총점과 평균
sum_subj = [0, 0, 0]
avg_subj = [0.0, 0.0, 0.0]

for std in student:
    sum_subj[0] += std["kor"]
    sum_subj[1] += std["eng"]
    sum_subj[2] += std["math"]

print("== 과목별 총점 ==")
print("국어 총점 : %d점" % sum_subj[0])
print("영어 총점 : %d점" % sum_subj[1])
print("수학 총점 : %d점" % sum_subj[2])


for std in student:
    avg_subj[0] = sum_subj[0] / len(student)
    avg_subj[1] = sum_subj[1] / len(student)
    avg_subj[2] = sum_subj[2] / len(student)
    
print("== 과목별 평균 ==")
print("국어 평균 : %.1f점" % avg_subj[0])
print("영어 평균 : %.1f점" % avg_subj[1])
print("수학 평균 : %.1f점" % avg_subj[2])

"""

# 용어 사전 만들기

print("♠ 용어 사전 ♠")
word = input("정의되어 있는 단어를 입력하세요: ")

dic = {
    "알고리즘": "어떤 문제를 해결하기 위해 정해진 일련의 절차",
    "이진수": "컴퓨터가 사용하는 0과 1만으로 이루어진 수",
    "버그": "프로그램이 적절하게 동작하는 데 실패하거나 오류가 발생하는 코드 조각"
}

# 예외 처리(비 정상적인 종료를 막아줌) : try ~ except 구문
try:
    definition = dic[word]
    print(definition)
except KeyError:
    print("정의된 단어가 없습니다.")





    





