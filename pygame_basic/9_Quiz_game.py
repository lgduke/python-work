# Quiz) 하늘에서 떨어지는 똥 피하기 게임
# 게임조건
# 1. 캐릭터는 화면 가장아래에 위치, 좌우로만 이동가능
# 2. 똥은 화면 가장위에서 떨어짐. X좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임종료
# 5. FPS는 30으로 고정

#[게임이미지]
# 배경 : 640*480(세로 가로) - 
# 캐릭터 : 70*70
# 똥 : 70 * 70

import random
import pygame
######################################################
#초기화. pygame 사용시 반드시 필요
pygame.init()

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Duke2 Ppappiyon Escape Game")
BLACK = ( 0, 0, 0 )

# FPS (Frame per second)
clock = pygame.time.Clock()
#####################################################

# 1. 사용자 게임 초기화(배경화면,게임이미지,좌표,폰트, 속도, )
# 배경 이미지 불러오기
backgroud = pygame.image.load\
    ("/Users/dukeh/Downloads/PythonWorkSpace/pygame_basic/background2.bmp")

# 캐릭터(스프라이트) 뿔러오기
character = pygame.image.load\
    ("/Users/dukeh/Downloads/PythonWorkSpace/pygame_basic/character.bmp")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐랙터의 가로크기
character_height = character_size[1] #캐랙터의 세로크기

character_x_pos = (screen_width / 2) - (character_width/ 2) # 화면 가로 크기의 절반에 위치하도록 설정
character_y_pos = screen_height - character_height # 화면 세로 크기의 가장 아래에 위치하도록 설정

# 이동할 좌표
to_x = 0

# 이동 속도
character_speed = 0.6

# 적(똥) 캐릭터 생성
ddong = pygame.image.load\
    ("/Users/dukeh/Downloads/PythonWorkSpace/pygame_basic/enemy.bmp")
ddong_size = ddong.get_rect().size #이미지의 크기를 구해옴
ddong_width = ddong_size[0] #캐랙터의 가로크기
ddong_height = ddong_size[1] #캐랙터의 세로크기
# 에네미 시작위치 선정

# print("random.randrange(1,(480-enemy_width)) is {0} - {1}".format(enemy_x_rand, enemy_width ))
ddong_x_pos = random.randint(0,screen_width-ddong_width) # 화면 가로 크기의 절반에 위치하도록 설정
ddong_y_pos = 0 # 화면 세로 크기의 가장 위에 위치하도록 설정
ddong_speed = 10

# 폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트, 크기)

# 총시간
total_time = 20

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

        if event.type == pygame.KEYDOWN: # 키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP: # 키가 띠어졌는지 확인
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               to_x = 0


# 3. 게임 캐릭터 위치 정의    
    character_x_pos += to_x * dt

#   가로 경계 값 처리
    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

# 3.1 Enemy 캐릭터 위치 정의
    ddong_y_pos += ddong_speed

#   세로 경계 값 처리
    if ddong_y_pos > screen_height:
        ddong_y_pos = 0
        ddong_x_pos = random.randint(0,screen_width-ddong_width)


# 4. 충돌처리
# 충돌처리를 위한 rect 정보 수정
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

# 충톨체크 
    if character_rect.colliderect(ddong_rect):
        print("Collide Wow !!!!!")
        text_Title2= game_font.render("Collide Now, Be careful", True, BLACK)
        screen.blit(text_Title2, [50, 100])
        pygame.display.flip() # 게임화면을 계속 다시그리기
        pygame.time.delay(2000)
        running = False

#. 5. 화면그리기  
#    screen.fill((0,0,255)) # R,G,B 각각 0~255 값을 가짐
    screen.blit(backgroud,(0,0)) #배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) #배경 그리기
    screen.blit(ddong,(ddong_x_pos,ddong_y_pos)) #배경 그리기

# 타이머 집어 넣기
# 경과 시간 계산
    elapsed_time = ( pygame.time.get_ticks() - start_ticks) / 1000
    # 경과시간 (ms) - 밀리세컨이라 초로 환산하기 위해 1000으로 나눔
    timer = game_font.render(str(int(total_time - elapsed_time)),True, (255,255,255))
    text_Title= game_font.render("Pygame Text Test", True, BLACK)
    screen.blit(text_Title, [50, 50])
    # 0.1초등 1단위 아래 숫자는 지우기 위해 int로 감쌈
    # render 함수는 출력할글자, True, 글자색상
    screen.blit(timer,(10, 10))

    # 화면에 타이머를 표시함

    if int(total_time - elapsed_time) <= 0:
        print("Time Out !!!!")
        running = False

    pygame.display.update() # 게임화면을 계속 다시그리기

# 잠시 종료전 대기 화면 표시
pygame.time.delay(2000)

# Pygame 종료
pygame.quit()