
import os
import tkinter as tk 
from tkinter import *
from PIL import ImageTk, Image


def btncmd():
    print("Button 7 is clicked !! ")



root = Tk() #main window
root.title("Nado GUI")

btn1 = Button(root, text="button1" )
btn1.pack()

btn2 = Button(root, padx=10, pady=5, text="button2------" )
btn2.pack()

btn3 = Button(root, padx=5, pady=10, text="button3------" )
btn3.pack()

btn4 = Button(root, width=10, height=3, text="button4" )
btn4.pack()

btn5 = Button(root, fg="red", bg="white" , text="button5" )
btn5.pack()

photo = ImageTk.PhotoImage(Image.open("gui_basic/img.bmp")) 
btn6 = Button(root, image=photo , text="button6" ) # 고정크기
btn6.pack()
 
btn7 = Button(root, text = "동작하는 버튼",command=btncmd)
btn7.pack()

root.mainloop()