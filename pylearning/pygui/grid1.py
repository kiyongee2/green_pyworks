from tkinter import *

window = Tk()
window.title('grid')
window.geometry("300x200")
window.option_add("*font", "바탕체 15")

# padx - x축 방향으로 여백 설정, pady - y축 방향으로 여백 설정
Button(window, text='(0, 0)').grid(row=0, column=0, padx=10)
Button(window, text='(0, 1)').grid(row=0, column=1, pady=10)
# columnspan - 셀 병합
Button(window, text='(1, 0)').grid(row=1, columnspan=2)
Button(window, text='(2, 0)').grid(row=2, column=0)

window.mainloop()
