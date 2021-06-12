# Project) 오락실 Pang 게임 만들기
# [게임조건]
# 1. 캐릭터는 화면 아래에 위치, 좌우로만 이동가능
# 2. 스페이스를 누르면 무기를 쏘아 올림
# 3. 큰 공1개가 나타나서 바운스
# 4. 무기에 닿으면 공은 작은 크기로 분활. 가장 작은 크기의 공은 사라짐
# 5. 모든공을 없애면 게임 종료(성공)
# 6. 캐릭터는 공에 닿으면 게임종료(실패)
# 7. 시간 제한 99초 초과시 게임 종료(실패)
# 8. FPS는 30으로 고정( 필요시 speed 값을 조정)
# [게임이미지]
# 1. 배경 : 640*480(가로*세로) - backgrounf
# 2. 무대 : 640 * 50 - stage
# 3. 캐릭터 : 33 * 60 - character
# 4. 무기 : 20 * 430 - weapon
# 5. 공 : 160*160, 80*80, 40*40, 20*20 - balloon1~4

import os
import pygame
#####################################################
# 초기화. pygame 사용시 반드시 필요
pygame.init()

#화면 크기 설정
screen_width = 640 # 가로 크기
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Nado Pang Game")

# FPS (Frame per second)
clock = pygame.time.Clock()
#####################################################

# 1. 사용자 게임 초기화(배경화면,게임이미지,좌표,폰트, 속도, )
# 폴더 설정
current_path = os.path.dirname(__file__) # 현재 위치한 디렉토리 회신
image_path = os.path.join(current_path,"images") #이미지 폴더 위치 반환
# 배경 이미지 불러오기
backgroud = pygame.image.load\
    (os.path.join(image_path, "background.bmp"))

# 스테이지 만들기 
stage = pygame.image.load\
    (os.path.join(image_path, "stage.bmp"))
stage_size = stage.get_rect().size
stage_height = stage_size[1] # 스테이지 높이위에 캐릭터를 두기 위해 사용

# 캐릭터 만들기
character = pygame.image.load\
    (os.path.join(image_path, "character.bmp"))
character_size = character.get_rect().size
character_width = character_size[0] 
character_height = character_size[1] # 스테이지 높이위에 캐릭터를 두기 위해 사용

character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height


# 이동할 좌표

# 이동 속도
character_speed = 0.6

# 적 캐릭터 생성

# 폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트, 크기)

# 총시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick 을 받아옴


# 이벤트 루프
running = True #게임이 진행주인가 ?
while running:
    dt = clock.tick(30) #  게임화면의 초당 프레임 수을 결정
    # 캐릭터가 100만큼 이동해야함
    # 10 fps : 1초 동안 10번 동작 -> 1번 프레임에 몇만큼 이동해야 하나 ->  10만큼 -> 10*10 = 100
    # 20 fps : 1초 동안 20번 동작 -> 1번 프레임에 몇만큼 이동해야 하나 ->  5만큼 -> 20*5 = 100

    # print("fps : " + str(clock.get_fps()))


# 2. 이벤트 처리(키보드 마우스)
    for event in pygame.event.get(): # 어떤 이벤트 발생하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False

    

# 3. 게임 캐릭터 위치 정의    

# 4. 충돌처리
# 충돌처리를 위한 rect 정보 수정

# 충톨체크 

#. 5. 화면그리기  
#    screen.fill((0,0,255)) # R,G,B 각각 0~255 값을 가짐
    screen.blit(backgroud,(0,0)) #배경 그리기
    screen.blit(stage,(0,screen_height - stage_height)) #배경 그리기
    screen.blit(character,(character_x_pos, character_y_pos))


# 타이머 집어 넣기
# 경과 시간 계산

    pygame.display.update() # 게임화면을 계속 다시그리기

# 잠시 종료전 대기 화면 표시
pygame.time.delay(2000)

# Pygame 종료
pygame.quit()