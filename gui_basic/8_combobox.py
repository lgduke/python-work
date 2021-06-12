import tkinter.ttk as ttk
from tkinter import *

def btncmd():
    print(combobox.get()) #선택된 값 출력
    print(rdonly_combobox.get())

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

values = [str(i)+" day" for i in range(1, 32) ] # 1~31 Values
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("Card Payment day")

rdonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly")
rdonly_combobox.current(0) #0번째 인덱스값 기본 선택
rdonly_combobox.pack()


btn = Button(root, text="SELECT",command=btncmd)
btn.pack()

root.mainloop() 