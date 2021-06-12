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
character_to_x = 0
# 이동 속도
character_speed = 5

# 무기 만들기
weapon = pygame.image.load\
    (os.path.join(image_path, "weapon.bmp"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0] 

# 무기는 한번에 여러발 발사 가능
weapons = []

# 무기 이동 속도
weapon_speed = 10

# 공만들기 (4개 크기에 대해 별도 처리)
ball_images = [
    pygame.image.load(os.path.join(image_path, "ballon1.bmp")),
    pygame.image.load(os.path.join(image_path, "ballon2.bmp")),
    pygame.image.load(os.path.join(image_path, "ballon3.bmp")),
    pygame.image.load(os.path.join(image_path, "ballon4.bmp")),
]

# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9] # 인덱스 0,1,2,3 에 해당하는 값
# 튕기고 올라갈때 값

# 공정보들
balls = []

# 최초 발생하는 큰 공 추가
balls.append({
    "pos_x" : 50, # 공의 X 좌표
    "pos_y" : 50, # 공의 Y 좌표 
    "img_idx" : 0 , # 어느 공의 좌표 인지.. 0은 제일 큰공
    "to_x" : 3 , # 공의 X축 이동방향 -3이면 왼쪽 +3이면 오른쪽
    "to_y" : -6 ,# Y축 이동방향
    "init_spd_y" : ball_speed_y[0] # Y의 최초속도 
})


# 폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트, 크기)

# 총시간
total_time = 10

# 시작 시간 정보
start_ticks = pygame.time.get_ticks() # 시작 tick 을 받아옴

# 충돌되어 사라질 무기, 공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #캐릭터가 왼쪽으로 이동
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT: #캐릭터가 오른쪽으로 이동
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE: # 무기를 발사
                weapon_x_pos = character_x_pos + (character_width/2) - (weapon_width/2)
                weapon_y_pos = character_x_pos
                weapons.append([weapon_x_pos,weapon_y_pos])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0
        
    # 3. 게임 캐릭터 위치 정의    
    character_x_pos += character_to_x

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치를 위로 올라가게 조정
    # 예) 초기 무기 위치 100,200 -> 180, 160, 140
    weapons = [ [w[0], w[1] - weapon_speed] for w in weapons ]
    # 천장에 닿은 무기 없애기 y축이 0보다 큰 놈만 리스트에 둔다
    weapons = [ [w[0], w[1]] for w in weapons if w[1] > 0 ]

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        ball_size = ball_images[ball_img_idx].get_rect().size
        ball_width = ball_size[0] 
        ball_height = ball_size[1] # 스테이지 높이위에 캐릭터를 두기 위해 사용
        
        # 가로벽에 닿았을때 공이동 위치 변경 (튕겨나오는 효과)
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1

        # 세로 위치
        # 스테이지에 튕겨서 올라가는 처리

        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else: # 그외의 모든 경우에는  속도를 줄여감
            ball_val["to_y"] += 0.5

        ball_val["pos_x"] += ball_val["to_x"]
        ball_val["pos_y"] += ball_val["to_y"]
        

    # 4. 충돌처리 
    # 충돌처리를 위한 rect 정보 수정
    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # 공 rect 정보 업테이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y
        # 공과 캐릭터의 충돌 처리
        if character_rect.colliderect(ball_rect):
            running = False
            break

        # 공과 무기들 충돌처리
        for weapon_idx, weapon_val in enumerate(weapons):
            weapon_pos_x = weapon_val[0]
            weapon_pos_y = weapon_val[1]
            # 무기 rect 정보 업테이트
            weapon_rect = weapon.get_rect()
            weapon_rect.left = weapon_pos_x
            weapon_rect.top = weapon_pos_y
            # 충톨체크       
            if weapon_rect.colliderect(ball_rect):
                weapon_to_remove = weapon_idx #해당 무기 없애기 위한 설정
                ball_to_remove = ball_idx #해당공 없애기 위한 설정
                break

    # 충돌된 공 , 무기 없애기
    if ball_to_remove > -1:
        del balls[ball_to_remove]
        ball_to_remove = -1
    if weapon_to_remove > -1:
        del weapons[weapon_idx]
        weapon_to_remove = -1

    #. 5. 화면그리기  
    #    screen.fill((0,0,255)) # R,G,B 각각 0~255 값을 가짐
    screen.blit(backgroud,(0,0)) #배경 그리기
    # 무기먼저 그려서 캐릭터를 가리지 않게..

    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon,(weapon_x_pos, weapon_y_pos))

    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x,ball_pos_y))
        


    screen.blit(stage,(0,screen_height - stage_height)) #배경 그리기
    screen.blit(character,(character_x_pos, character_y_pos))



# 타이머 집어 넣기
# 경과 시간 계산

    pygame.display.update() # 게임화면을 계속 다시그리기

# 잠시 종료전 대기 화면 표시
pygame.time.delay(2000)

# Pygame 종료
pygame.quit()