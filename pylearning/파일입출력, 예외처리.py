import random, time
# 파일 쓰기 및 읽기
"""
f = open("./output/file1.txt", 'w')
f.write("메모장에 기록")
f.close()

f = open("./output/file1.txt", 'r')
data = f.read()
print(data)
f.close()

with open("./output/hello.txt") as f:
    data = f.read()
    print(data)
"""
# 숫자 자료형 쓰기
"""
f = open('c:/pyfile/number.txt', 'w')
#f.write(300) - 오류
f.write('300\n')
f.write('10.7\n')
f.write(str(300) + '\n')
num = 12 * 5
#f.write(str(num)+'\n')
f.write(f'{num}\n')
f.close()
"""

# 한 줄 읽기
"""
f = open('c:/pyfile/number.txt', 'r')
#data = f.read()
#print(data)
while True:
    line = f.readline()
    if not line:
        break
    print(line, end='')
f.close()
"""

# 반복 자료 쓰기
"""
f = open('c:/pyfile/repeat.txt', 'w')
for i in range(1, 11):
    #f.write(str(i) + ' ')
    data = f'{i}번째 줄입니다.\n'
    f.write(data)
f.close()

f = open('c:/pyfile/repeat.txt', 'r')
#text = f.read()
#print(text)
count = 0
while True:
    line = f.readline()
    if not line:
        break
    count += 1
    print(line, end='')
print(f'줄 수는 {count}개')
"""
# 리스트 저장
"""
seasons = ["봄", "여름", "가을", "겨울"]
with open("./output/season2.txt", 'w') as f:
    for i in seasons:
        f.write(i + ' ')
    #for i in range(len(seasons)):
        #f.write(seasons[i] + ' ')

with open("./output/season2.txt", 'r') as f:
    #data = f.read()
    #print(data)
    #랜덤 읽기
    list = f.read().split()
    season = random.choice(list)
    print(season)
"""

# 단어 쓰기 및 랜덤 읽기
"""
with open("./output/word.txt", 'w') as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree',
            'strawberry', 'grape', 'garlic', 'onion', 'patato']

    for i in word:
        f.write(i + ' ')
"""
"""
with open('./output/word.txt', 'r') as f:
    data = f.read().split()
    print(data)
    for i in data:
        print(i)
    word = random.choice(data)
    print(word)
"""

# 입력받아 파일 쓰기
try:
    with open("./output/input.txt", 'a') as f:
        while True:
            text = input("저장할 내용을 입력해 주세요(종료-z) : ")
            if text == 'z' or text == 'Z':
                break
            f.write(text)
            f.write('\n')
except:
    print("파일을 찾을 수 없습니다.")

# 바이너리 파일(이미지) 읽고 쓰기
"""
with open('./output/data.bin', 'wb') as f:
    text = "비가 내린다."
    #f.write(text) # type error(object)
    f.write(text.encode())

with open('./output/data.bin', 'rb') as f:
    data = f.read()
    print(data)
    print(data.decode())

with open('activity.jpg', 'rb') as f1:
    img = f1.read()

with open('./output/activity2.jpg', 'wb') as f2:
    f2.write(img)
"""

# 타자 연습 게임
"""
try:
    with open('./output/word.txt') as f:
        word = f.read().split()
        #print(random.choice(word))
    n = 1  #문제 번호
    input("[타자 게임] 준비되면 엔터를 치세요")
    start = time.time()
    while n <= 10:
        question = random.choice(word)
        print(f'문제 {n}')
        print(question)  # 문제
        user = input()   # 사용자 입력
        if question == user:
            print("통과!!")
            n += 1
        else:
            print("오타!! 다시 도전")
    end = time.time()
    print(f"게임 소요 시간 : {end-start:.2f}초")
    #print("게임을 종료합니다.")
except:
    print("파일을 찾을 수 없습니다.")
"""

