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

        # Radio 버튼
        # 레이아웃 - 버튼 2개를 올릴 프레임을 만듬
        radio_frame = Frame(frame)
        radio_selection = StringVar()
        b1 = Radiobutton(radio_frame, text="left",
                    variable=radio_selection, value='L')
        b1.pack(side=LEFT)
        b2 = Radiobutton(radio_frame, text="right",
                    variable=radio_selection, value='R')
        b2.pack(side=RIGHT)
        radio_frame.grid(row=1, column=2)

root = Tk()
root.title("UI 구성")

app = App(root)

# 온도 변환기 test1
"""
class App:
    def __init__(self, root):
        frame = Frame(root)
        frame.pack()

        Label(frame, text='deg C').grid(row=0, column=0)
        Button(frame, text='변환', command=self.convert).grid(row=1, columnspan=2)

    def convert(self):
        print("구현되지 않음")

root = Tk()
root.title("TempConverter")

app = App(root)
"""

# 온도 변환기 구현
"""
# 1inch = 25.4mm
class ScaleConverter:
    def __init__(self, units_from, units_to, factor):
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    def convert(self, value):
        return self.factor * value

if __name__ == "__main__":
    con = ScaleConverter("inches", "mm", 25)
    print("Converting 2 inches")
    # print(str(con.convert(2)) + con.units_to)
    print(f'{con.convert(2)}{con.units_to}')

    con2 = ScaleConverter("KB", "B", 1024)
    print("Converting 1 KB")
    print(str(con2.convert(1)) + con.units_to)

# 단위 변환 클래스
# F = C x 1.8 + 32
class Converter(ScaleConverter):
    def __init__(self, units_from, units_to, factor, offset):
        super().__init__(units_from, units_to, factor)
        self.offset = offset

    def convert(self, value):
        return self.factor * value + self.offset

conv = Converter('C', 'F', 1.8, 32)
print("Convert 20C")
#print(str(conv.convert(20)) + conv.units_to)
print(f'{conv.convert(21):.2f}{conv.units_to}')

class App:
    def __init__(self, root):
        self.con = Converter('C', 'F', 1.8, 32)
        frame = Frame(root)
        frame.pack()

        Label(frame, text='deg C').grid(row=0, column=0)
        self.c = DoubleVar()
        Entry(frame, textvariable=self.c).grid(row=0, column=1)

        Label(frame, text='deg F').grid(row=1, column=0)
        self.f = DoubleVar()
        Label(frame, textvariable=self.f).grid(row=1, column=1)
        Button(frame, text='변환', command=self.convert).grid(row=2, columnspan=2)

    def convert(self):
        c = self.c.get()
        con_f = self.con.convert(c) # 화씨온도로 변환
        con_f = f'{con_f:.2f}F'
        self.f.set(con_f)  # 계산된 화씨온도를 레이블에 출력

root = Tk()
root.title("Temperature Converter")
root.geometry("250x100")

app = App(root)

root.mainloop()
"""
# 계산기 숫자 버튼 테스트
"""
def click1():
    display.insert(END, '1')

def click2():
    display.insert(END, '2')

root = Tk()
root.title("나의 계산기")

display = Text(root, width=20, height=1, bg='light green')
display.grid(row=0, column=0)

Button(root, text='1', width=5, command=click1).grid(row=1, column=0)
Button(root, text='2', width=5, command=click2).grid(row=2, column=0)
"""

# 계산기 만들기
"""
root = Tk()
root.title("나의 계산기")

# top_row 프레임
top_row = Frame(root)
top_row.grid(row=0, column=0, columnspan=2, sticky=N)

display = Entry(top_row, width=50, bg='light green')
display.grid(row=0, column=0)

def click(key):
    if key == '=':
        try:
            value = eval(display.get())
            result = str(value)[0:10]
            display.insert(END, '=' + result)
        except:
            display.insert(END, '-->오류')
    elif key == 'C':
        display.delete(0, END)
    else:
        display.insert(END, key)

# 숫자 버튼 프레임
num_pad = Frame(root)
num_pad.grid(row=1, column=0, sticky=W)
num_pad_list = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0', '.', '=',
]
r = 0
c = 0
for btn_txt in num_pad_list:
    def cmd(x=btn_txt):
        click(x)

    Button(num_pad, text=btn_txt, width=5, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 2:
        c = 0
        r = r + 1

# 연산자 버튼 프레임
operator = Frame(root)
operator.grid(row=1, column=1, sticky=E)
operator_list = [
    '*', '/',
    '+', '-',
    '(', ')',
    'C']
r = 0
c = 0
for btn_txt in operator_list:
    def cmd(x=btn_txt):
        click(x)

    Button(operator, text=btn_txt, width=5, command=cmd).grid(row=r, column=c)
    c = c + 1
    if c > 1:
        c = 0
        r = r + 1
"""

root.mainloop()