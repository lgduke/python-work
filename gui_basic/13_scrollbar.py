import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

#
listbox = Listbox(frame, selectmode="extended", height=10, \
yscrollcommand=scrollbar.set)

for i in range(1,32):
    listbox.insert(END, str(i)+"day" )
listbox.pack(side="left") 

scrollbar.config(command=listbox.yview)

root.mainloop() 