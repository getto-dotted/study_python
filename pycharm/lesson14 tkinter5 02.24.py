from tkinter import *

def process1():
    entry1['bg'] = 'yellow'
    lbl2['font'] = '궁서체 16 italic'
    entry1.configure({'bg':'yellow', "fg":'red'})

def process():
    temp = float(entry1.get())
    changeTemp = (temp-32) * 5/9
    entry2.insert(0, changeTemp)
    entry2.configure({'bg': 'yellow', "fg": 'red'})
win = Tk()

lbl1 = Label(win, text='화씨', font='궁서체 14')
btn1 = Button(win, text='화씨->섭씨', command=process)
entry1 = Entry(win)

lbl2 = Label(win, text='섭씨', font='궁서체 14')
btn2 = Button(win, text='섭씨->화씨')
entry2 = Entry(win)

lbl1.grid(row=0, column=0)
entry1.grid(row=0, column=1)
btn1.grid(row=2, column=0)

lbl2.grid(row=1, column=0)
entry2.grid(row=1, column=1)
btn2.grid(row=2, column=1)

entry1.insert(0, '0') # 엔트리(인덱스, 스트링)
entry2.insert(0, '0')

if __name__ == '__main__':
    win.mainloop()
