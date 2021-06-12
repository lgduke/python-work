from tkinter import *

def btncmd():
    print(chkvar.get()) # 0 : 체크해제 , 1 : 체크
    print(chkvar2.get())
    # print("chkvar1 is {0} - chkvar2 is {1}".format(chkvar, chkvar2 ))

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

chkvar = IntVar() #chkvar에 int형으로 값을 저장한다 
chkbox = Checkbutton(root, text="Don't look today", variable=chkvar)
chkbox.select() #자동 선택 처리
chkbox.deselect() #선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="Don't look for one week!!", variable=chkvar2)
chkbox2.pack()


btn = Button(root, text="click ~~",command=btncmd)
btn.pack()

root.mainloop()