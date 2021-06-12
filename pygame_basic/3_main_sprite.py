import pygame

#초기화. pygame 사용시 반드시 필요
pygame.init()

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Duke Game")

# 배경 이미지 불러오기
backgroud = pygame.image.load\
    ("/Users/dukeh/Downloads/PythonWorkSpace/pygame_basic/background1.bmp")

# 캐릭터(스프라이트) 뿔러오기
character = pygame.image.load\
    ("/Users/dukeh/Downloads/PythonWorkSpace/pygame_basic/character.bmp")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐랙터의 가로크기
character_height = character_size[1] #캐랙터의 세로크기

character_x_pos = (screen_width / 2) - (character_width/ 2) # 화면 가로 크기의 절반에 위치하도록 설정
character_y_pos = screen_height - character_height # 화면 세로 크기의 가장 아래에 위치하도록 설정

# 이벤트 루프
running = True #게임이 진행주인가 ?
while running:
    for event in pygame.event.get(): # 어떤 이벤트 발생하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False
#    screen.fill((0,0,255)) # R,G,B 각각 0~255 값을 가짐
    screen.blit(backgroud,(0,0)) #배경 그리기
    screen.blit(character,(character_x_pos,character_y_pos)) #배경 그리기

    pygame.display.update() # 게임화면을 계속 다시그리기

# Pygame 종료
pygame.quit()