import pygame as pg 

screen_width = 800
screen_height = 600
pg.init()
screen = pg.display.set_mode((screen_width, screen_height))

player_x = 400
player_y = 300

clock = pg.time.Clock()
running = True
speed = 1
black_color = (0,0,0)
powder_blue_color=(102,255,255)
while running:
    fps = clock.tick(100)
    for event in pg.event.get():
        if event.type == pg.QUIT:            
            running=False
    key_event = pg.key.get_pressed()
    if key_event[pg.K_LEFT]:
        player_x -= speed*fps
    if key_event[pg.K_RIGHT]:
        player_x += speed*fps
    if key_event[pg.K_UP]:
        player_y -= speed*fps
    if key_event[pg.K_DOWN]:
        player_y += speed*fps

    screen.fill(black_color)
    pg.draw.circle(screen,powder_blue_color,(player_x,player_y),10)
    pg.display.update()
pg.quit()