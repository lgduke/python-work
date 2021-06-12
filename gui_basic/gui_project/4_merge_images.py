import tkinter.ttk as ttk # combo, radiobutton 사용을 위해
import tkinter.messagebox as msgbox # message box 사용을 위해
import os

from tkinter import *
from tkinter import filedialog # file 창 사용
from PIL import Image


root = Tk()
root.title("Nado GUI")

# 파일 추가 함수
def add_file():
    files = filedialog.askopenfilenames(title="이미지 화일을 선택하세요",\
        filetypes=(("PNG file","*.png"),("all file","*.*")),\
        initialdir="C://") #최초에 C:/ 경로를 보여줌

    # 사용자가 선택한 화일 목록
    for file in files:
        list_file.insert(END, file)
# 선택 삭제
def del_file():
    # print(list_file.curselection()) 
    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장경로 함수(폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "" : #사용자가 선택하지 않고 취소를 누름
        return
    # print(folder_selected)
    txt_dest_path.delete(0, END) 
    txt_dest_path.insert(0, folder_selected)

# 이미지 통합
def merge_image():
    print(list_file.get(0, END))
    images = [Image.open(x) for x in list_file.get(0,END)]
    # size -> size[0] : width, size[1] : height
    #[(10,10),(20,20),(30,30)] - ex
    # widths = [x.size[0] for x in images]
    # heights = [x.size[1] for x in images]

    widths, heights = zip(*(x.size for x in images))

    # 최대 넓이, 전체 높이 구해옴
    
    max_width, total_height = max(widths), sum(heights)
    print("max_width : ", max_width)
    print("max_heights : ", total_height)

    print("widths : ", widths)
    print("heights : ", heights)

    # 스케치북 준비
    result_img = Image.new("RGB",(max_width,total_height),(255,255,255) ) #배경 흰색
    y_offset = 0 # 붙이는 이미지 시작하는 높이 위치
    # for img in images:
    #     result_img.paste(img,(0, y_offset))
    #     y_offset += img.size[1]

    for idx, img in enumerate(images):
        result_img.paste(img,(0, y_offset))
        y_offset += img.size[1]

        progress = (idx+1) / len(images) * 100 # 현재 처리중인 사진 인덱스로 처리양 계산
        p_var.set(progress)
        progress_bar.update()

    dest_path = os.path.join(txt_dest_path.get(), "duke_photo.jpg")
    result_img.save(dest_path)
    msgbox.showinfo("Info","Work is done. Good luck")

# 시작
def start():
    #각 옵션 값 확인시작
    print("가로 넓이 : ", cmb_width.get())
    print("간격 : ", cmb_space.get())
    print("사이즈 : ", cmb_format.get()) 
    # 화일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("Warning","Add image files  !! ")
        return
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning("Warning","Add folder to save  !! ")
        return
    
    # 이미지 통합 작업
    merge_image()

    

# 파일 프레임. (파일추가, 삭제) 
file_frame = Frame(root)
file_frame.pack(fill="x", padx =5, pady =5 ) #간격 뛰우기 

btn_add_file = Button(file_frame, padx=5, pady =5, width=12, \
    text="add file", command=add_file)
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx=5, pady =5, width=12, \
    text="del file", command=del_file)
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

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=browse_dest_path)
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

btn_start = Button(frame_run, padx=5, pady=5, text="RUN", width=12,command=start)
btn_close = Button(frame_run, padx=5, pady=5, text="CLOSE", \
    width=12, command=root.quit)
btn_close.pack(side="right",padx =5, pady =5) # pack 하는  순서대로 오른족에 나옴
btn_start.pack(side="right",padx =5, pady =5)





root.resizable(False,False) # X, Y 값 변경 불가. 창크기 변경 불가
root.mainloop()  