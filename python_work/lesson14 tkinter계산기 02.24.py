from time import time, sleep
from tkinter import *
import time

cal_list = '' # 연산기호 저장
temp_cal = '' # 숫자 저장

def inputNum(num):
    if num == 'C': # 클리어 버튼을 눌렀을 때
        entry.delete(0,'end') # entry의 내용을 모두 지운다
        entry.insert('end',0) # entry에 0을 넣는다.
        entry2.delete(0, 'end') # entry2의 내용을 모두 지운다
        entry2.insert('end', 0) # entry2에 0을 넣는다.

    else: # 최초입력시 & 숫자버튼 및 .(소수점) 버튼을 눌렀을 때
        entry.delete(0, 'end') # entry의 내용을 모두 지운다
        entry.insert('end', num) # entry에 해당 버튼의 값을 넣는다.


def inputCal(cal): # 사칙연산 기호 입력시
    global cal_list # 전역변수 cal_list
    global temp_cal # 전역변수 temp_cal
    if not entry.get() in ['0','+','-','/','*','.']:  # 기존에 입력한 숫자가 있을때만 연산버튼 인식 //연산버튼을 2회 연속 누르기x
        cal_list = cal # 현재 입력한 사친연산기호
        temp_cal = float(entry.get())  # 입력된 숫자를 float로 형변환하여 임시변수로 옮긴다
        entry.delete(0, 'end')  # 입력칸을 비우고, 다음숫자를 입력받을 준비.
        entry2.insert(0, str(temp_cal)+str(cal)) # 제2입력칸에 내가 입력한 숫자와 연산기호를 표시해 준다.

def eval():
    global cal_list #전역변수 cal_list
    global temp_cal # 전역변수 temp_cal

    if not (cal_list =='' and entry.get()==''): # 사칙연산 기호가 저장되어 있고 새로운 숫자가 있을때 실행(연산자는 숫자 없이 쓰일 수 없으므로 숫자,연산자,숫자일 때) 
        number = float(entry.get()) # 새로입력한 수를 가져옴 
        if cal_list == '/':
            solution = temp_cal/number
        elif cal_list == '*':
            solution = temp_cal*number
        elif cal_list == '+':
            solution = temp_cal+number
        else :
            solution = temp_cal-number

        # 계산후, entry, entry2 및 전연변수들을 비우고, 계산결과를 표시.
        entry.delete(0,'end')
        entry.insert(0,solution)
        entry2.insert(0, solution)
        cal_list = ''
        temp_cal = 0

#=====================================================================================================

win = Tk()

entry = Entry(win, width=62, bg = 'yellow', justify='right') # justify='right' /center/left 텍스트 정렬
entry2 = Entry(win, width=62, justify='right')

entry.insert(0,0) # 기본으로 0을 넣어줌
entry2.insert(0,0)

entry.grid(row=1, column=0,columnspan=5)
entry2.grid(row=0, column=0,columnspan=5)

btn0 = Button(win, text ='0', width=10, command= lambda : inputNum('0')).grid(row = 5, column=1)
btn1 = Button(win, text ='1', width=10, command= lambda : inputNum('1')).grid(row = 4, column=0)
btn2 = Button(win, text ='2', width=10, command= lambda : inputNum('2')).grid(row = 4, column=1)
btn3 = Button(win, text ='3', width=10, command= lambda : inputNum('3')).grid(row = 4, column=2)
btn4 = Button(win, text ='4', width=10, command= lambda : inputNum('4')).grid(row = 3, column=0)
btn5 = Button(win, text ='5', width=10, command= lambda : inputNum('5')).grid(row = 3, column=1)
btn6 = Button(win, text ='6', width=10, command= lambda : inputNum('6')).grid(row = 3, column=2)
btn7 = Button(win, text ='7', width=10, command= lambda : inputNum('7')).grid(row = 2, column=0)
btn8 = Button(win, text ='8', width=10, command= lambda : inputNum('8')).grid(row = 2, column=1)
btn9 = Button(win, text ='9', width=10, command= lambda : inputNum('9')).grid(row = 2, column=2)
btn_dot = Button(win, text ='.', width=10, command= lambda : inputNum('.')).grid(row = 5, column=0)
btn_clear = Button(win, text ='c', width=10, height=7, command= lambda : inputNum('C')).grid(row = 2, column=4, rowspan=4)

btn_sum = Button(win, text ='+', width=10, command= lambda : inputCal('+')).grid(row = 2, column=3)
btn_sub = Button(win, text ='-', width=10, command= lambda : inputCal('-')).grid(row = 3, column=3)
btn_mul = Button(win, text ='×', width=10, command= lambda : inputCal('*')).grid(row = 4, column=3)
btn_div = Button(win, text ='÷', width=10, command= lambda : inputCal('/')).grid(row = 5, column=3)

btn_equal = Button(win, text ='=', width=10, command= lambda : eval()).grid(row = 5, column=2)

if __name__ == '__main__':
    win.mainloop()
