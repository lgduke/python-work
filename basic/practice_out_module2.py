# glob : 경로내의 폴더 / 화일 목록 조회
import glob
print(glob.glob("*.py")) #확장자가 py인 모든화일에 대해 알려줌. 

# os :운영체제에서 제공하는 기본 기능
import os
# print(os.getcwd()) #현재 디렉토리 표시

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("Folder is already existed")
#     os.rmdir(folder)
#     print(folder,"Folder is removed")
# else:
#     os.makedirs(folder) #폴더 생성
#     print(folder,"Folder is created")

# print(os.listdir())

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d-%a %H:%M:%S"))

import datetime
print("오늘 날짜는 ", datetime.date.today())

#timedelta : 두날짜사이의 간격
today = datetime.date.today() #오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 이후 
print("TD", today)
print("TD2", td)
print("우리가 만난지 100일은 ", today + td)



