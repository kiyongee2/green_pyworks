import os

os.chdir("c:/pyfile")  #pyfile 디렉터리로 이동

dir = os.popen('dir')  #dir 명령어 실행 - 목록을 메모리에 저장

print(dir.read())      # dir 읽기
