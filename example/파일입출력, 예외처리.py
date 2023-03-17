# 파일 쓰기 및 읽기
f = open("./output/hello.txt", 'w')
f.write("Hello~ Python!!")
f.close()

f = open("./output/hello.txt", 'r')
data = f.read()
print(data)
f.close()


"""
season = ["봄", "여름", "가을", "겨울"]
with open("./output/season.txt", 'w') as f:
    for i in season:
        f.write(i + ' ')


with open("./output/season.txt", 'r') as f:
    data = f.read()
    print(data)
"""
