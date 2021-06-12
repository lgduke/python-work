import time
import tkinter.ttk as ttk
from tkinter import *

def btncmd():
    progressbar.stop()
def btncmd1():
    progressbar.start(10)
def btncmd2():
    for i in range(1 ,101): #1부터 100
        time.sleep(0.01) #0.01초 대기

        p_var2.set(i) # progress bar의 값을 설정
        progressbar2.update() #ui update
        print(p_var2.get())

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")

# progressbar.start(10) #10ms 마다 움직임
# progressbar.pack()

p_var2 = DoubleVar() 
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

btn = Button(root, text="START",command=btncmd2)
btn.pack()
# btn1 = Button(root, text="AGAIN",command=btncmd1)
# btn1.pack()


root.mainloop() 