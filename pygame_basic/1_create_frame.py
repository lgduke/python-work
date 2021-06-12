import pygame

#초기화. pygame 사용시 반드시 필요
pygame.init()

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screeen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Duke Game")

# 이벤트 루프
running = True #게임이 진행주인가 ?
while running:
    for event in pygame.event.get(): # 어떤 이벤트 발생하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트 발생
            running = False

# Pygame 종료
pygame.quit()