# Quiz:tkinter를 이용한 메모장프로그램을 만드시오
#
# 1. title : 제목없음 - windows 메모장
# 2. 메뉴 : 파일,편집,서식, 보기, 도움말
# 3. 실제 메뉴 구현 : 파일 메뉴에서 열기. 저장, 끝내기 3개만 처리
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기
# 3-2. 저장 : mynote.txt 파일에 현재 내용 저장하기
# 3-3. 끝내기 : 프로그램 종료
# 4. 프로그램 시작시 본문은 비어 있는 상태
# 5. 하단 status 바는 필요없음
# 6. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능
# 7. 본문 우측에 상하 스크롤바 넣기

import tkinter.messagebox as msgbox
from tkinter import *

def open_file():
    print("Open mynote.txt")

def save_file():
    print("save mynote.txt")

root = Tk()
root.title("제목없음 - windows 메모장")
root.geometry("640x480") #가로 세로 크기 정의

menu = Menu(root)
# File Menu
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="Open File",command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit",command=root.quit)

menu.add_cascade(label="File" ,menu=menu_file )
editmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editmenu)
tempmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Template" , menu=tempmenu)
viewmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="View",menu=viewmenu )
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help" , menu=helpmenu)

root.config(menu=menu)

# 스크롤바 
# frame = Frame(root)
# frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# 텍스트 입력창

txt = Text(root, width=640, height=480, yscrollcommand=scrollbar.set)
txt.pack()
txt.insert(END,"Write here")

scrollbar.config(command=txt.yview)






root.mainloop() 