from tkinter import *

win = Tk()

lbl1 = Label(win, text='화씨')
btn1 = Button(win, text='화씨->섭씨')
entry1 = Entry(win)

lbl2 = Label(win, text='섭씨')
btn2 = Button(win, text='섭씨->화씨')
entry2 = Entry(win)

lbl1.place(x=0, y=0)
entry1.place(x=40, y=0)
btn1.place(x=220, y=0)

lbl2.place(x=0, y=30)
entry2.place(x=40, y=30)
btn2.place(x=220, y=30)

entry1.insert(0, '0') # 엔트리(인덱스, 스트링)
entry2.insert(0, '0')

if __name__ == '__main__':
    win.mainloop()
