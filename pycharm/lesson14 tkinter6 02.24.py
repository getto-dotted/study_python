from tkinter import *

def change_img():
    path = entry.get()
    print('이미지 교체 기능 실행', path)
    img = PhotoImage(file=path)
    imgLabel.configure({'image':img})
    imgLabel.image = img

win = Tk()

photo = PhotoImage(file="굿럭.png")
imgLabel = Label(win, image=photo)
imgLabel.pack()

entry =Entry(win)
entry.pack()

btn = Button(win, text ="사진교체", command=change_img)
btn.pack()

if __name__ == '__main__':
    win.mainloop()
