# 점심 쿠폰
import random
from tkinter import *

def click():
    namelist = ['이진성', '노승우', '박성호', '권지혜', '김은효',
                '이경철', '성의석', '이유진', '유성길', '한주훈',
                '강정현', '김현우', '이영준', '안재훈', '김민정',
                '유세현', '윤기은', '오화룡', '조은별', '이가은']

    winner = []

    while len(winner) < 4:
        name = random.choice(namelist)
        if name not in winner:
            winner.append(name)

    # 출력
    output.delete(0.0, END)
    output.insert(END, winner)

    # print(winner)

"""
# randint() 사용
while len(winner) < 4:
    idx = random.randint(0, 19)
    if idx not in winner:
        winner.append(idx)
        
# for i in winner:
#     print(namelist[i], end='')
"""

window = Tk()
window.title("쿠폰 추첨기")
window.option_add('*font', '맑은고딕 13')

# 이미지 넣기
lbl_img = Label(window)
img = PhotoImage(file = "bronx.png")
lbl_img.config(image = img)
lbl_img.grid(row=0, column=0, sticky=W)

# 추첨 버튼
Button(window, text='추첨', command=click).grid(row=1, column=0, sticky=E)

# 이름 출력
output = Text(window, width=41, height=4, bg='yellow')
output.grid(row=2, column=0, sticky=W)

window.mainloop()
