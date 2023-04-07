# 클래스
"""
class Student:
    def __init__(self):
        self.name = "콩쥐"
        self.grade = 1
        print("생성자 함수")

    def learn(self):
        print("수업을 듣습니다.")

s = Student() # 객체 생성
print(s.name, "학생은", s.grade, "학년입니다.")
s.learn()
print(s)  # 객체 출력
print(type(s)) # 자료형 : 클래스
"""

# 생성자(constructor)
"""
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def learn(self):
        print("수업을 듣습니다.")

s1 = Student("김하나", 1)
print(s1.name, "학생은", s1.grade, "학년입니다.")
s1.learn()

s2 = Student("이둘", 3)
#print(s2.name + " 학생은 " + str(s2.grade) + "학년입니다.")
print(f'{s2.name} 학생은 {s2.grade}학년입니다.')
s2.learn()

# __str__(self)
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def learn(self):
        print("수업을 듣습니다.")

    def __str__(self):
        #return "이름 : {}, 학년 : {}".format(self.name, self.grade)
        return "이름 : " + self.name + ", 학년 : " + str(self.grade)

if __name__ == "__main__":
    s1 = Student("김하나", 1)
    print(s1)
    s1.learn()

    s2 = Student("이둘", 3)
    print(s2)
    s2.learn()
"""

# 기본 생성자 - 생략 가능
"""
class AirPlane:
    def __init__(self):
        pass

    def take_off(self):
        print("비행기가 이륙합니다.")

    def fly(self):
        print("비행기가 일반 비행합니다.")

    def land(self):
        print("비행기가 착륙합니다.")


plane = AirPlane()
plane.take_off()
plane.fly()
plane.land()
"""

# 계산기 클래스
"""
class Calculator:
    def __init__(self):
        self.x = 0

    def add(self, y):
        self.x = self.x + y
        return self.x

    def sub(self, y):
        self.x = self.x - y
        return self.x

c1 = Calculator()
print(c1.add(10))
print(c1.sub(4))
"""

# 인스턴스 리스트
"""
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

dog1 = Dog("기쁨")
dog2 = Dog("사랑")

dog1.add_trick('몸 뒤집기')
print(dog1.tricks)

dog2.add_trick("죽은 척 하기")
print(dog2.tricks)

# 정적(고정) 클래스

class Dog:
    kind = "진돗개"  #클래스 변수

    def __init__(self, name):
        self.name = name  # 인스턴스 변수

dog1 = Dog("백구")
dog2 = Dog("검둥이")

print(dog1.name)  # dog1만 유일
print(dog2.name)  # dog2만 유일

# 모든 dog이 공유
print(dog1.kind)
print(dog2.kind)
# 클래스 이름으로 직접 접근(올바른 유형)
print(Dog.kind)

# 클래스 리스트
class Cart:
    li = []

    def __init__(self, goods):
        Cart.li.append(goods)

    def __str__(self):
        return Cart.li

cart1 = Cart("계란")
print(cart1.li)

cart2 = Cart("두부")
print(cart2.li)

cart3 = Cart("커피")
print(cart3.li)


# 전체 요소 출력
for i in Cart.li:
    print(i)
"""

# 클래스 리스트 인덱싱
"""
class City:
    a = ['Seoul', 'Incheon', 'Daejon', 'Jeju']

str = ''
for i in City.a:
    str = str + i[0]

print(str)
"""

# 상속(inheritance)
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def get_id(self):
        return self.employee_id

e1 = Employee("김산", 25, 101)
print("이름 :", e1.get_name())
print("나이 :", e1.get_age())
print("사원번호 :", e1.get_id())
"""

# 초음속 비행기
"""
class AirPlane:
    def __init__(self):
        pass

    def take_off(self):
        print("비행기가 이륙합니다.")

    def fly(self):
        print("비행기가 일반 비행합니다.")

    def land(self):
        print("비행기가 착륙합니다.")

class SuperSonicAirPlane(AirPlane):
    NORMAL = 1
    SUPERSONIC = 2

    def __init__(self):
        self.fly_mode = SuperSonicAirPlane.NORMAL

    def fly(self):  # 메서드 재정의
        if self.fly_mode == SuperSonicAirPlane.SUPERSONIC:
            print("비행기가 초음속으로 비행합니다.")
        else:
            super().fly()

sa = SuperSonicAirPlane()
sa.take_off()
sa.fly()
sa.fly_mode = SuperSonicAirPlane.SUPERSONIC
sa.fly()
sa.fly_mode = SuperSonicAirPlane.NORMAL
sa.fly()
sa.land()
"""

# 단위 변환 클래스(상속)
# 1inch = 25.4mm

class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, value):
        return self.factor * value

if __name__ == "__main__":
    con = ScaleConverter("inches", "mm", 25)
    print("Converting 2 inches")
    # print(str(con.convert(2)) + con.units_to)
    print(f'{con.convert(2)}{con.units_to}')

# 단위 변환 클래스
# F = C x 1.8 + 32
class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)
        self.offset = offset

    def convert(self, value):
        return self.factor * value + self.offset

conv = Converter('C', 'F', 1.8, 32)
print("Convert 20C")
#print(str(conv.convert(20)) + conv.units_to)
print(f'{conv.convert(21):.2f}{conv.units_to}')
    


        








