import time
import tkinter.ttk as ttk # combo, radiobutton 사용을 위해
import tkinter.messagebox as msgbox # message box 사용을 위해
import os

from tkinter import *
from tkinter import filedialog # file 창 사용
from PIL import Image
from PIL import ImageGrab

def start():
    time.sleep(2) #5초 대기 : 사용자가 준비하는 시간

    for i in range(1,2): #2초 간격으로 10개 이미지 저장
        img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
        img.save("image{}.png".format(i)) # 파일로 저장
        time.sleep(2) # 2초 간격
    
    msgbox.showinfo("Info","Work is done. Good luck")


root = Tk()
root.title("ScreenShot GUI")

# 파일 프레임. (파일추가, 삭제) 
file_frame = Frame(root)
file_frame.pack(fill="x", padx =5, pady =5 ) #간격 뛰우기 

btn_start = Button(file_frame, padx=5, pady=5, text="RUN", width=12,command=start)
btn_close = Button(file_frame, padx=5, pady=5, text="CLOSE", \
    width=12, command=root.quit)
btn_close.pack(side="right",padx =5, pady =5) # pack 하는  순서대로 오른족에 나옴
btn_start.pack(side="right",padx =5, pady =5)

root.resizable(False,False) # X, Y 값 변경 불가. 창크기 변경 불가
root.mainloop()  