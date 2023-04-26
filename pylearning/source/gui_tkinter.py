# 창 만들고 버튼 클릭하면 콘솔에 문자 출력
from tkinter import *
"""
def click():
    print("안녕~ 파이썬")

root = Tk()
root.title("hello")
root.geometry("200x60+300+100")

frame = Frame(root)
frame.pack()

Label(frame, text="Hello~ python").grid(row=0, column=0)
Button(frame, text='확인', command=click).grid(row=1, column=0)

root.mainloop()
"""
# 글자를 입력받아 그대로 출력하기
"""
def click():
    text = entry.get()
    output.delete(0.0, END) #0.0 - 줄번호, 시작문자
    output.insert(END, text) # END - 문자열이 입력된 최종지점

root = Tk()
root.title("이름 입력")
Label(root, text="이름 : ").grid(row=0, column=0)
entry = Entry(root, width=10)
entry.grid(row=0, column=1)
Button(root, text="확인", command=click).grid(row=1, columnspan=2)
output = Text(root, width=20, height=5)
output.grid(row=2, columnspan=2)

root.mainloop()
"""

# 용어 사전 만들기

def click():
    try:
        word = entry.get()
        output.delete(0.0, END)
        definition = dic[word]
        output.insert(END, definition)
    except:
        output.insert(END, "단어의 정의를 찾을 수 없습니다.")

dic = {
    "알고리즘": "컴퓨터로 작업을 수행하기 위해 컴퓨터가 이해할 수 있도록 단계별로 설명해 놓은 것",
    "버그": "프로그램이 적절하게 동작하는데 실패하거나 또는 전혀 동작하지 않는 원인을 제공하는 코드 조각",
    "이진수": "2진법으로 나타낸 숳자, 0과 1로 구성됨"
}

root = Tk()
root.title("용어 사전")

Label(root, text="단어를 입력하고 엔터 키를 누르세요").grid(row=0,
                    column=0, sticky=W)
entry = Entry(root, width=20, bg="lightgreen")
entry.grid(row=1, column=0, sticky=W)
Button(root, text="제출", width=10, command=click).grid(row=2,
                    column=0, sticky=W)
Label(root, text="정의").grid(row=0, column=0, sticky=W)
output = Text(root, width=80, height=10, bg="lightgreen")
output.grid(row=4, column=0, sticky=W)

root.mainloop()
