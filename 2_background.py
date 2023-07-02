import pygame

pygame.init() #초기화

#화면 크기 설정
screen_width = 480 
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("mtak game") #게임 이름

#배경 이미지 불러오기
background = pygame.image.load("C:/Users/192293/pythonGame/background.png")

# 이벤트 루프
running = True #게임이 진행중인가?

while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생했나?
        if event.type == pygame.QUIT: # 'x'버튼 눌렀는가?
            running = False #게임이 진행중이 아님
    
    # screen.fill((100, 150, 150))
    screen.blit(background, (0, 0)) # 배경 그리기 #무엇을, 어디에 뿌릴건지
    
    pygame.display.update() #게임화면을 다시 그리기


#pygame 종료
pygame.quit()