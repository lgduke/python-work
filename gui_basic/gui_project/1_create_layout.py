import tkinter.ttk as ttk # combo, radiobutton 사용을 위해
from tkinter import *

root = Tk()
root.title("Nado GUI")

# 파일 프레임. (파일추가, 삭제) 
file_frame = Frame(root)
file_frame.pack(fill="x", padx =5, pady =5 ) #간격 뛰우기 

btn_add_file = Button(file_frame, padx=5, pady =5, width=12, text="add file")
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx=5, pady =5, width=12, text="del file")
btn_del_file.pack(side="right")

# 리스트 프레임.
list_frame = Frame(root)
list_frame.pack(fill="both",padx =5, pady =5)

scrollbar=Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y") # fill - 위아래로 쭉 펼쳐지는 스크롤바

list_file = Listbox(list_frame, selectmode="extended" , \
     height=15, yscrollcommand=scrollbar.set) 
list_file.pack(side="left", fill="both", expand=True) # fill - 위아래 좌우로 펼쳐짐
scrollbar.config(comman=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text="저장경로" )
path_frame.pack(fill="x",padx =5, pady =5,ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, padx =5, pady =5, ipady=4)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right",padx =5, pady =5)

# 옵션 프레임
frame_option = LabelFrame(root, text="Option") 
frame_option.pack(padx =5, pady =5,ipady=5)
 
# 가로 넓이 옵션
# 가로 넓이 레이블 
lbl_width = Label(frame_option, text="가로넓이", width=8)
lbl_width.pack(side="left",padx =5, pady =5)
# 가로 넓이 콤보
opt_width = ["Original","1024","800","640"]
cmb_width = ttk.Combobox(frame_option,state="readonly",\
    values=opt_width, width=10)
cmb_width.current(0) #첫번째 값을 default로 함
cmb_width.pack(side="left",padx =5, pady =5)

# 간격 옵션
# 간격 옵션 레이블
lbl_space = Label(frame_option, text="간격", width=8)
lbl_space.pack(side="left",padx =5, pady =5)
# 간격 옵션 콤보
opt_space = ["없음", "좁게",  "보통" , "넓게"]
cmb_space = ttk.Combobox(frame_option,state="readonly",\
    values=opt_space, width=10)
cmb_space.current(0) #첫번째 값을 default로 함
cmb_space.pack(side="left",padx =5, pady =5)

# 파일 포맷 옵션
# 파일 포맷 옵션 레이블
lbl_format = Label(frame_option, text="format", width=8)
lbl_format.pack(side="left",padx =5, pady =5)
# 파일 포맷 옵션 콤보
opt_format = ["png", "jpg",  "bmp"]
cmb_format = ttk.Combobox(frame_option,state="readonly",\
    values=opt_format, width=10)
cmb_format.current(0) #첫번째 값을 default로 함
cmb_format.pack(side="left",padx =5, pady =5)


# 진행상황 (progress bar)
frame_progress = LabelFrame(root, text="Progress")
frame_progress.pack(fill="x",padx =5, pady =5,ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, \
    variable= p_var )
progress_bar.pack(fill="x",padx =5, pady =5)

# 실행 프레임. 시작과 닫기 버튼
frame_run = LabelFrame(root, text="Action")
frame_run.pack(fill="x",padx =5, pady =5)

btn_start = Button(frame_run, padx=5, pady=5, text="RUN", width=12)
btn_close = Button(frame_run, padx=5, pady=5, text="CLOSE", \
    width=12, command=root.quit)
btn_close.pack(side="right",padx =5, pady =5) # pack 하는  순서대로 오른족에 나옴
btn_start.pack(side="right",padx =5, pady =5)





root.resizable(False,False) # X, Y 값 변경 불가. 창크기 변경 불가
root.mainloop()  