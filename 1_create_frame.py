import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("mtak game") #게임 이름

# 이벤트 루프
running = True #게임이 진행중인가?

while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT: # 'x'버튼 눌렀는가?
            running = False

#pygame 종료
pygame.quit()