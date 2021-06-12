import pygame

#초기화. pygame 사용시 반드시 필요
pygame.init()

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Duke Game")

# FPS (Frame per second)
clock = pygame.time.Clock()

# 배경 이미지 불러오기
backgroud = pygame.image.load\
    ("/Users/dukeh/Downloads/PythonWorkSpace/pygame_basic/background.bmp")

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
to_y = 0

# 이동 속도
character_speed = 0.6

# 적 캐릭터 생성
enemy = pygame.image.load\
    ("/Users/dukeh/Downloads/PythonWorkSpace/pygame_basic/enemy.bmp")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0] #캐랙터의 가로크기
enemy_height = enemy_size[1] #캐랙터의 세로크기

enemy_x_pos = (screen_width / 2) - (enemy_width/2) # 화면 가로 크기의 절반에 위치하도록 설정
enemy_y_pos = (screen_height /2) - (enemy_height/2) # 화면 세로 크기의 가장 아래에 위치하도록 설정


# 이벤트 루프
running = True #게임이 진행주인가 ?
while running:
    dt = clock.tick(60) #  게임화면의 초당 프레임 수을 결정
    # 캐릭터가 100만큼 이동해야함
    # 10 fps : 1초 동안 10번 동작 -> 1번 프레임에 몇만큼 이동해야 하나 ->  10만큼 -> 10*10 = 100
    # 20 fps : 1초 동안 20번 동작 -> 1번 프레임에 몇만큼 이동해야 하나 ->  5만큼 -> 20*5 = 100

    # print("fps : " + str(clock.get_fps()))

    for event in pygame.event.get(): # 어떤 이벤트 발생하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False

        if event.type == pygame.KEYDOWN: # 키가 눌려졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            if event.key == pygame.K_RIGHT:
                to_x += character_speed
            if event.key == pygame.K_UP:
                to_y -= character_speed
            if event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP: # 키가 띠어졌는지 확인
           if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
               to_x = 0
           if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
               to_y = 0
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
#   가로 경계 값 처리
    if character_x_pos < 0:
        character_x_pos =0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
#   세로 경계 값 처리
    if character_y_pos < 0:
        character_y_pos =0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

# 충돌처리를 위한 rect 정보 수정
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

# 충톨체크 
    if character_rect.colliderect(enemy_rect):
        print("Collide Wow !!!!!")
        running = False
               
#    screen.fill((0,0,255)) # R,G,B 각각 0~255 값을 가짐
    screen.blit(backgroud,(0,0)) #배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) #배경 그리기
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos)) #배경 그리기

    pygame.display.update() # 게임화면을 계속 다시그리기

# Pygame 종료
pygame.quit()