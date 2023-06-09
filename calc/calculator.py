# 계산기 만들기
from tkinter import *

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

root.mainloop()
