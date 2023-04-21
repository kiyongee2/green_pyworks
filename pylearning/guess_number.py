# 숫자 추측 게임(Up And Down Game)
# 컴퓨터가 임의의 숫자 생각함
# 사람이 컴퓨터가 생각한 숫자보다 크면 "너무 커요"
# 작으면 "너무 작아요", 맞추면 "정답!!"
import random

com = random.randint(1, 100)
min_v = 1
max_v = 100

while True:
    guess = int(input(f"맞혀보세요({min_v} ~ {max_v})? ")) #사람이 추측한 숫자 입력
    if guess == com:
        print("정답!!")
        break
    elif guess > com:
        print("너무 커요")
        max_v = guess
    else:
        print("너무 작아요")
        min_v = guess