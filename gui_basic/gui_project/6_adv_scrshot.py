
from PIL import ImageGrab
import keyboard
import time

def screenshot():
    # _20200601_102030 
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab() # 현재 스크린 이미지를 가져옴
    img.save("image{}.png".format(curr_time)) # 파일로 저장

# keyboard.add_hotkey("F9", screenshot) #사용자가 F9를 누르면 저장
keyboard.add_hotkey("a", screenshot) #사용자가 a를 누르면 저장
# keyboard.add_hotkey("ctrl+shift+s", screenshot) 

keyboard.wait("esc", screenshot) #사용자가 esc를 누를때까지 수행
