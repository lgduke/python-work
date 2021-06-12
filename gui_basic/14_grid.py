import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

btn1 = Button(root, text="button1")
btn2 = Button(root, text="button2")

# btn1.pack()
# btn2.pack()

# btn1.pack(side="left")
# btn2.pack(side="right")
# btn1.grid(row=0,column=0)
# btn2.grid(row=1,column=1)

# 계산기 맨 윗줄
btn_f16 = Button(root,text="F16",width=5, height=1)
btn_f17 = Button(root,text="F17",width=5, height=1)
btn_f18 = Button(root,text="F18",width=5, height=1)
btn_f19 = Button(root,text="F19",width=5, height=1)

btn_f16.grid(row=0,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0,column=3, sticky=N+E+W+S, padx=3, pady=3)

# clear 줄
btn_clear = Button(root,text="Clear",width=5, height=1)
btn_eq = Button(root,text="=",width=5, height=1)
btn_div = Button(root,text="/",width=5, height=1)
btn_mul = Button(root,text="*",width=5, height=1)

btn_clear.grid(row=1,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_eq.grid(row=1,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 7 줄
btn_7 = Button(root,text="7",width=5, height=1)
btn_8 = Button(root,text="8",width=5, height=1)
btn_9 = Button(root,text="9",width=5, height=1)
btn_sub = Button(root,text="-",width=5, height=1)

btn_7.grid(row=2,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 4 줄
btn_4 = Button(root,text="4",width=5, height=1)
btn_5 = Button(root,text="5",width=5, height=1)
btn_6 = Button(root,text="6",width=5, height=1)
btn_add = Button(root,text="+",width=5, height=1)

btn_4.grid(row=3,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3,column=3, sticky=N+E+W+S, padx=3, pady=3)

# 1 줄
btn_1 = Button(root,text="1",width=5, height=1)
btn_2 = Button(root,text="2",width=5, height=1)
btn_3 = Button(root,text="3",width=5, height=1)
btn_en = Button(root,text="Enter",width=5, height=1)

btn_1.grid(row=4,column=0, sticky=N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4,column=1, sticky=N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4,column=2, sticky=N+E+W+S, padx=3, pady=3)
btn_en.grid(row=4,column=3, rowspan=2, sticky=N+E+W+S, padx=3, pady=3) #현재 위치로 부터 아래쪽으로 숫자만큼을 더함

# 0 줄
btn_0 = Button(root,text="0",width=5, height=1)
btn_point = Button(root,text=".",width=5, height=1)

btn_0.grid(row=5,column=0,columnspan=2, sticky=N+E+W+S, padx=3, pady=3)
btn_point.grid(row=5,column=2, sticky=N+E+W+S, padx=3, pady=3)


root.mainloop() 