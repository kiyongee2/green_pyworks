from tkinter import *
import datetime

# root = Tk()
# root.geometry("300x200") # 너비 x 높이
# root.title("처음 만드는 윈도우")

# 윈도우
"""
# 버튼
btn = Button(root, text='버튼', font=("맑은고딕", 20))
btn.pack()  #가운데 정렬
"""

# 버튼 이벤트
"""
def click():
    # print("안녕~ 파이썬!")
    demo.config(text="안녕, 파이썬!")

root.option_add("*Font", "맑은고딕 15")
frame = Frame(root)
frame.pack()

Label(frame, text="").grid(row=0, column=0)
Label(frame, text="Hello Python!!").grid(row=1, column=0)
Label(frame, text="").grid(row=2, column=0)
#Button(frame, text="확인").grid(row=3, column=0)
Button(frame, text="확인", command=click).grid(row=3, column=0)
Label(frame, text="").grid(row=4, column=0)
demo = Label(frame)
demo.grid(row=5, column=0)
"""

# 현재 시각
"""
def get_time():
    now = datetime.datetime.today()
    # print(now.strftime("%H:%M:%S AM"))
    display = now.strftime("%H:%M:%S AM")
    output.insert(END, display)

root.option_add("*Font", "맑은고딕 15")
frame = Frame(root)
frame.pack()

Label(frame, text="").grid(row=0, column=0)
Label(frame, text="Hello Python!!").grid(row=1, column=0)
Label(frame, text="").grid(row=2, column=0)
#Button(frame, text="확인").grid(row=3, column=0)
Button(frame, text="확인", command=click).grid(row=3, column=0)
output = Label(frame)
output.grid(row=4, column=0)
# output = Text(frame, width=12, height=2)
# Label(frame, text="").grid(row=4, column=0)
# output.grid(row=5, column=0)
"""

# 용어 사전
"""
def select():
    try:
        word = entry.get()
        definition = dic[word]
        # 0.0 - 첫째행, 첫째 열(문자위치), 이전 내용 삭제
        output.delete(0.0, END)
        output.insert(END, definition)
    except:
        output.insert(END, "단어의 정의를 찾을 수 없습니다.")

dic = {
        "알고리즘": "어떤 문제를 해결하기 위해 정해진 일련의 절차",
        "이진수": "컴퓨터가 사용하는 0과 1만으로 이루어진 수",
        "버그": "프로그램이 적절하게 동작하는 데 실패하거나 오류가 발생하는 코드 조각"
}

root = Tk()
root.title("용어 사전")

lbl = Label(root)
lbl.config(text="단어를 입력하고 엔터 키를 누르세요")
lbl.grid(row=0, column=0, sticky=W)
entry = Entry(root, width=20, bg="yellowgreen")
entry.grid(row=1, column=0, sticky=W)
btn = Button(root, command=select)
btn.config(text="제출")
btn.grid(row=2, column=0, sticky=W)
Label(root, text="정의").grid(row=3, column=0, sticky=W)
output = Text(root, width=80, height=10, bg="yellowgreen")
output.grid(row=4, column=0, sticky=W)
"""

# 위젯 - 컨트롤 도구
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        Label(frame, text="제목").grid(row=0, column=0)
        Entry(frame, width=28).grid(row=0, column=1)
        Button(frame, text="확인").grid(row=0, column=2)

        #check 버튼
        check_var = StringVar()
        check = Checkbutton(frame, text="체크 버튼")
        check.config(variable=check_var, onvalue='Y', offvalue='N')
        check.grid(row=1, column=0)

        # 리스트 목록
        listbox = Listbox(frame, height=3, selectmode=SINGLE)
        for item in ['red', 'green', 'blue', 'yellow']:
            listbox.insert(END, item)
        listbox.grid(row=1, column=1)

root = Tk()
root.title("UI 구성")

app = App(root)

root.mainloop()
