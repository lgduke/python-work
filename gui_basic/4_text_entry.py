from tkinter import *

def btncmd():
    print(txt.get("1.0", END)) # 1 line 0 Col 부터 txt를 가지고 와라
    print(e.get())
    # 내용 삭제
    txt.delete("1.0",END)
    e.delete(0,END)


root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

txt = Text(root, width=30, height=5)
txt.pack()
txt.insert(END,"Write here")

e = Entry(root, width=30) # 1줄로만 입력가능 엔터 안됨 
e.pack()
e.insert(0,"Only One line !!")
 
btn = Button(root, text="click ~~",command=btncmd)
btn.pack()

root.mainloop()