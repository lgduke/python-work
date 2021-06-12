from tkinter import *

def btncmd():
    print(burger_var.get()) #행버거중 선택된 라디오 항목의 값을 반환
    print(drink_var.get()) #행버거중 선택된 라디오 항목의 값을 반환

root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

Label(root, text="Choose the menu~").pack()
# label1.pack()

burger_var = IntVar() #여기에 int형으로 저장
btn_burger1 = Radiobutton(root, text="Hamburger", value=1, variable=burger_var)
btn_burger1.select() # Hamburger를 기본값 설정
btn_burger2 = Radiobutton(root, text="Cheese burger", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="Chicken burger", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root, text="Choose the drink~").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="cola", value="cola", variable=drink_var)
btn_drink1.select() #cola를 기본값 설정
btn_drink2 = Radiobutton(root, text="cider", value="cider", variable=drink_var)
btn_drink3 = Radiobutton(root, text="fanta", value="fanta", variable=drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


btn = Button(root, text="ORDER",command=btncmd)
btn.pack()

root.mainloop() 