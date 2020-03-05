from time import time, sleep
from tkinter import *
import time



def paint(event):
    x, y = event.x, event.y
    x2, y2 = x+1,y+1
    canvas.create_oval(x,y,x2,y2, fill='black')

win = Tk()

canvas = Canvas(win)
canvas.pack()
canvas.bind("<B1-Motion>", paint)


if __name__ == '__main__':
    win.mainloop()
