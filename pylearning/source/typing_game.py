# 영어 타자 게임 - 외부파일(단어장)
import random, time

try:
    f = open('c:/pyfile/words.txt', 'r')
    data = f.read().split()
    #print(word)
    f.close()

    n = 1   #문제 번호
    input('[타자 게임] 준비되면 엔터!')
    start = time.time()    # 현재까지의 시간(시작시간)
    while n <= 10:
        question = random.choice(data) # 컴퓨터가 제시한 단어
        print(f'문제 {n}')
        print(question)
        user = input()  # 게이머가 입력
        if question == user: # 오타가 없으면
            print("통과")
            n = n + 1   # 문제번호 1 증가
        else:
            print("오타, 다시 도전!")
    end = time.time()   # 종료시간
    print(f'게임 소요 시간 : {end-start:.2f}초')
except:
    print("파일을 찾을수 없습니다.")