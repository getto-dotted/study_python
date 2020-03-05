from tkinter import  *

win = Tk()
btn = Button(win, text = '클릭')
btn.pack()
btn = Button(win, text = '클릭')
btn.pack() # 주어진 컨테이너에 순서대로 객체를 붙임

if __name__ == '__main__':
    win.mainloop()