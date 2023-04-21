# 영어 단어장 - words.txt
try:
    words = ['ant', 'bear', 'chicken', 'dog', 'eagle', 'fox',
             'horse', 'lion', 'mouse', 'monkey', 'tiger']
    f = open("c:/pyfile/words.txt", 'w')
    for i in words:
        f.write(i + ' ')
    f.close()
except:
    print("파일을 쓰는데 실패했습니다.")