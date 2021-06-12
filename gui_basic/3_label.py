
import os
import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image

def change():
    label1.config(text="See you again!!")
    global photo2
    photo2 = ImageTk.PhotoImage(Image.open("gui_basic/imgx1.bmp")) 
    label2.config(image=photo2)
    

root = Tk() #main window
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

label1 = Label(root, text="Hello !!!! ")
label1.pack()

photo = ImageTk.PhotoImage(Image.open("gui_basic/img.bmp")) 
label2 = Label(root, image=photo , text="Hello2 !!!" ) # 고정크기
label2.pack()

btn = Button(root,text="Click", command=change)
btn.pack()

root.mainloop() 