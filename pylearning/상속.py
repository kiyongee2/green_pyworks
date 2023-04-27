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
"""
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
    
    con2 = ScaleConverter("KB", "B", 1024)
    print("Converting 1 KB")
    print(str(con2.convert(1)) + con.units_to)

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
"""

# 계산기 -> 확장 계산기
"""
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mul(self):
        return self.x * self.y

    def div(self):
        return self.x / self.y

if __name__=="__main__":
    cal = Calculator(5, 0)
    print(cal.add())
    print(cal.sub())
    print(cal.mul())
    print(cal.div())

class MoreCalculator(Calculator):
    # 2x2x2x2
    def pow(self):
        num = 1
        for i in range(0, self.y):
            num = num * self.x
        return num

    def pow(self):
        return self.x ** self.y

    def div(self):
        if self.y == 0:
            return 0  #0으로 종료
        else:
            return self.x / self.y

        try:
            return self.x / self.y
        except ZeroDivisionError as e:
            # return "0으로 나눌 수 없습니다."
            return e

cal1 = MoreCalculator(2, 4)
print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal1.div())
print(cal1.pow())

cal2 = MoreCalculator(4, 0)
print(cal1.add())
print(cal1.sub())
print(cal1.mul())
print(cal2.div())  # 0
print(cal2.pow())
"""

class Customer:
    def __init__(self, cid, name):
        self.cid = cid          #고객 아이디
        self.name = name        #고객 이름
        self.cgrade = "SILVER"  #고객 등급
        self.bonus_point = 0    #보너스 포인트
        self.bonus_ratio = 0.01 #보너스 적립율 - 1%
        # print("생성자 함수")

    def calc_price(self, price):  # 가격 및 보너스 포인트 계산
        #보너스포인트 = 보너스 포인트 + (가격 x 보너스적립율)
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def getname(self):  #고객의 이름을 반환하는 메서드
        return self.name

    def __str__(self):
        return self.name + "님의 등급은 " + self.cgrade + \
               "이고, 보너스 포인트는 " + str(self.bonus_point) + "점 입니다."

if __name__ == "__main__":
    silver = Customer(1001, "정국")
    price = 10000
    cost = silver.calc_price(price)
    print(silver.getname() + "님의 구매 비용은 " + str(cost) + "원 입니다.")
    print(silver)

class GoldCustomer(Customer):
    def __init__(self, cid, name):
        super().__init__(cid, name) #고객 아이디와 이름은 상속받음
        self.cgrade = "GOLD"        #고객 등급
        self.sale_ratio = 0.1       #구매 할인율
        self.bonus_ratio = 0.02     #보너스 적립율

    def calc_price(self, price):
        price -= int(price * self.sale_ratio) #할인 가격 = 가격 x 구매 할인율
        self.bonus_point += int(price * self.bonus_ratio)
        return price

if __name__ == "__main__":
    gold = GoldCustomer(1002, '지민')
    price = 10000
    cost = gold.calc_price(price)
    print(gold.getname() + "님의 구매 비용은 " + str(cost) + "원 입니다.")
    print(gold)

class VIPCustomer(Customer):
    # vip 고객 - 전문 상담원(agent)
    def __init__(self, cid, name, agent):
        super().__init__(cid, name)
        self.agent = agent
        self.cgrade = "VIP"     # 고객 등급
        self.sale_ratio = 0.1   # 구매 할인율
        self.bonus_ratio = 0.05 # 보너스적립율

    def calc_price(self, price):  #함수 이름은 같고 내용이 다름(재정의)
        #할인된 가격 = 가격 x 구매 할인율
        price -= int(price * self.sale_ratio)
        self.bonus_point += int(price * self.bonus_ratio)
        return price

    def __str__(self):
        return super().__str__() + "\n상담원 ID는 " \
               + str(self.agent) + "입니다."

if __name__ == "__main__":
    vip = VIPCustomer(1004, "RM", 777)
    price = 10000
    cost = vip.calc_price(price)
    print(vip.getname() + "님의 구매 비용은 " + str(cost) + "원입니다.")
    print(vip)  # 객체의 정보 출력

# 고객 관리
silver = Customer(101, "놀부")
gold = GoldCustomer(102, "흥부")
vip = VIPCustomer(103, "심청", 7777)

price = 10000
# 상품 가격 계산
cost_s = silver.calc_price(price)
cost_g = gold.calc_price(price)
cost_v = vip.calc_price(price)

print("********** 상품 구매 비용 **********")
print(silver.getname() + "님의 구매 비용은 " + str(cost_s) + "원입니다.")
print(gold.getname() + "님의 구매 비용은 " + str(cost_g) + "원입니다.")
print(vip.getname() + "님의 구매 비용은 " + str(cost_g) + "원입니다.")

print("******************** 고객 정보 ********************")
print(silver)
print(gold)
print(vip)

# 고객 관리 리스트
# 객체 리스트 생성
customer = [
    Customer(101, "놀부"),
    Customer(102, "팥쥐"),
    GoldCustomer(201, "흥부"),
    GoldCustomer(202, "콩쥐"),
    VIPCustomer(301, "심청", 777)
]

# 상품 가격 계산
price = 10000
print("********** 구매 비용 **********")
for c in customer:
    cost = c.calc_price(price)
    #print(c.getname() + "님의 구매비용은 " + str(cost) + "원입니다.")
    print(c.getname() + "님의 구매비용은 " + format(cost, ',d') + "원입니다.")

print("**************** 고객 정보 ***************")
for c in customer:
    print(c)

