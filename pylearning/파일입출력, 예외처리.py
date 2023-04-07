import random
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

# 리스트 저장
"""
season = ["봄", "여름", "가을", "겨울"]
with open("./output/season2.txt", 'w') as f:
    for i in season:
        f.write(i + ' ')

with open("./output/season2.txt", 'r') as f:
    data = f.read()
    print(data)
"""
"""
with open("./output/word.txt", 'w') as f:
    word = ['sky', 'earth', 'moon', 'flower', 'tree',
            'strawberry', 'grape', 'garlic', 'onion', 'patato']

    for i in word:
        f.write(i + ' ')
"""

with open('./output/word.txt', 'r') as f:
    data = f.read().split()
    print(data)
    for i in data:
        print(i)
    word = random.choice(data)
    print(word)