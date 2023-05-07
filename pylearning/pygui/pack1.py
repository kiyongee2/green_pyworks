from tkinter import *

window = Tk()
window.title('pack')
window.geometry("300x100")
window.option_add("*font", "바탕체 15")

Label(window, text='안녕하세요').pack()
btn =Button(window)
btn.config(text='확인')
# btn.pack(side='top')  #top(위), bottom(아래)
btn.pack(side='left')   #left(왼쪽), right(오른쪽)

window.mainloop()
