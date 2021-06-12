import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

def info():
    msgbox.showinfo("알림","정상적으로 예매되었읍니다!")
def warn():
    msgbox.showwarning("경고","매진되었읍니다. !")
def error():
    msgbox.showerror("에라","결제오류가 발생하였읍니다.. !")
def okcancel():
    msgbox.askokcancel("확인취소","해당좌석은 유아동반석입니다. 예매하겠읍니까? ")
def retrycancel():
    response = msgbox.askretrycancel("재시도취소","일시적 오류입니다. 다시 시도하겠읍니까? ")
    print("Response is - ", response) # True, False, None
    # 예 - 1, 아니오 - 2, 취소는 그외의 숫자
    if response == 1: # retry
        print("Yes")
    elif response == 0: #cancel
        print("No")
    
def yesno():
    msgbox.askyesno("예/아니오","역방향 좌석입니다.예매하겠읍니까? ")
def yesnocancel():
    response = msgbox.askyesnocancel(title=None ,message=\
        "예매내역이 저장되지 않았읍니다. \n 저장후 종효하시겠읍니까? ")
    # 네 : 저장후 종료
    # 아니오 : 저장하지 않고 종료
    # 취소 : 프로그램 취소
    print("Response is - ", response) # True, False, None
    # 예 - 1, 아니오 - 2, 취소는 그외의 숫자
    if response == 1:
        print("Yes")
    elif response == 0:
        print("No")
    else:
        print("Cancel")





Button(root,command=info, text="알림").pack()
Button(root,command=warn, text="경고").pack()
Button(root,command=error, text="에라").pack()
Button(root,command=okcancel, text="확인취소").pack()
Button(root,command=retrycancel, text="재시도취소").pack()
Button(root,command=yesno, text="예/아니오").pack()
Button(root,command=yesnocancel, text="예/아니오/취소").pack()


root.mainloop() 