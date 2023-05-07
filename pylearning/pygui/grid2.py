from tkinter import *

window = Tk()
window.title('grid')
window.geometry("300x200")
window.option_add("*font", "바탕체 15")

# sticky= W(서쪽), E(동쪽), N(북쪽), S(남쪽)
Label(window, text='오늘도 좋은 하루 되세요!').grid(row=0, column=0, sticky=E)
Button(window, text='북').grid(row=1, column=0, sticky=N)
Button(window, text='서').grid(row=2, column=0, sticky=W)
Button(window, text='동').grid(row=2, column=1, sticky=E)
Button(window, text='남').grid(row=3, column=0, sticky=S)

window.mainloop()

