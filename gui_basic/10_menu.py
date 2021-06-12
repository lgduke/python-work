
from tkinter import *

def create_new_file():
    print("Making a new file")

def create_new_win():
    print("Making a new window")


root = Tk()
root.title("Nado GUI")
root.geometry("640x480") #가로 세로 크기 정의

menu = Menu(root)

# File Menu

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New File",command=create_new_file)
menu_file.add_command(label="New Window")
menu_file.add_separator()
menu_file.add_command(label="Open File..")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable")
menu_file.add_separator()
menu_file.add_command(label="Exit",command=root.quit)

menu.add_cascade(label="File",menu=menu_file )

# Edit Menu
editmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit",menu=editmenu)

# language Menu 추가 (라디오 버튼)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="JSP")

menu.add_cascade(label="language",menu=menu_lang)

# view Menu 추가 (check box)
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")

menu.add_cascade(label="view",menu=menu_view)



root.config(menu=menu)

root.mainloop() 