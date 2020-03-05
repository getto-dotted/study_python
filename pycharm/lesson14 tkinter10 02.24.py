from time import time, sleep
from tkinter import *
import time

cal_list = []
show_list = []

def sum():
    cal_list.append('+')
def sub():
    cal_list.append('-')
def mul():
    cal_list.append('*')
def div():
    cal_list.append('/')

def inputNum(num):
    print(num)

win = Tk()

entry = Entry(win, width=60, bg = 'yellow')

btn_list = ['7','8','9','/','C','4','5','6','*','','1','2','3','-','','0','.','=','+','']
rowidx = 1
colidx = 0
for btn in btn_list:
    Button(win, text=btn, width=10, command = lambda: inputNum(btn)).grid(row=rowidx, column=colidx)
    colidx += 1
    if colidx >4 :
        rowidx += 1
        colidx = 0

entry.grid(row=0, column=0,columnspan=5)

'딕셔너리를 만들고 딕셔너리의 키값을 버튼값으로 //리스트에서 눌려진 찾기'

if __name__ == '__main__':
    win.mainloop()
