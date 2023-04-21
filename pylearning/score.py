# 리스트 생성 및 연산
score = [70, 80, 60, 100, 90]
sum_v = 0

# 유형1
# i = score[0]
for i in score:
    sum_v += i
    print("i =", i)

# 평균 = 총점 / 개수
avg_v = sum_v / len(score)

print("총점: ", sum_v)
print("평균: ", avg_v)