from tkinter import *

win = Tk()

lbl1 = Label(win, text='화씨')
btn1 = Button(win, text='화씨->섭씨')
entry1 = Entry(win)

lbl2 = Label(win, text='섭씨')
btn2 = Button(win, text='섭씨->화씨')
entry2 = Entry(win)

lbl1.pack()
entry1.pack()
btn1.pack()

lbl2.pack()
entry2.pack()
btn2.pack()

entry1.insert(0, '화씨입력') # 엔트리(인덱스, 스트링)
entry2.insert(0, '섭씨입력')

if __name__ == '__main__':
    win.mainloop()
