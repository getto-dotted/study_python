from time import time, sleep
from tkinter import *
import time

myColor = 'blue'

def change_color():
    global myColor
    if myColor == 'red':
        myColor = 'blue'
    else:
        myColor = 'red'

def paint(event):
    x, y = event.x, event.y
    x2, y2 = x+1,y+1
    #canvas.create_oval(x,y,x2,y2, fill=myColor, outline = myColor)
    canvas.create_polygon(x, y, x2, y2, fill=myColor, outline=myColor)


win = Tk()

canvas = Canvas(win)
canvas.pack()
canvas.bind("<B1-Motion>", paint)

btn = Button(win, text='색바꾸기', command=change_color)
btn.pack()

if __name__ == '__main__':
    win.mainloop()
