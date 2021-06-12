import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

Label(root, text="Choose the menu").pack(side="top")
Button(root,text="Order").pack(side="bottom")

# 버거 프레임
frame_burger = Frame(root, relief="solid",bd = 1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="Hamburger").pack()
Button(frame_burger, text="Cheeseburger").pack()
Button(frame_burger, text="Chikenburger").pack()


# 드링크 프레임
frame_drink = LabelFrame(root, text="drink")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="Cola").pack()
Button(frame_drink, text="Sprite").pack()

root.mainloop() 