from tkinter import *

def btncmd():
    # listbox.delete(END) #맨뒤 항목을 삭제
    # listbox.delete(0) #맨앞 항목을 삭제

    # 갯수 확인
    # print("In List are -- ",listbox.size(), "existed")
    
    # 항목 확인(시작, 끝을 입력 )
    # print("First to Third are ",listbox.get(0,2))

    # 선책 항목 확인(위치 반환, 0,2,3 등)
    print("Selected one are ",listbox.curselection())


root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

listbox = Listbox(root, selectmode="extended",height=0) 
#listbox = Listbox(root, selectmode="single",height=0) 

#extended option 여러개 선택가능, single 한개만 선택 가능
# 0은 리스트를 전체를 다보이게. 3이면 3개만 보이게

listbox.insert(0,"apple")
listbox.insert(1,"strawberry")
listbox.insert(2,"banana")
listbox.insert(END ,"watermelon")
listbox.insert(END ,"grape")
listbox.pack()

btn = Button(root, text="click ~~",command=btncmd)
btn.pack()

root.mainloop()