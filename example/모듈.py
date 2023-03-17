# 모듈(클래스) 사용하기
from my_module import Student

# 인스턴스 2개 생성
s1 = Student("이순신", 1)
print(s1)
s1.learn()

s2 = Student("권율", 3)
print(s2)
s2.learn()

# 객체 배열(리스트) 생성
student = [
    Student("김하나", 1),
    Student("이둘", 2),
    Student("박셋", 3)
]

print("***** 학생 명단 *****")
for s in student:
    print(s)
