import pygame
pygame.init() #initialize

SIZE = WIDTH, HEIGHT = 1000, 600
SCREEN = pygame.display.set_mode(SIZE)

WHITE = 255,255,255#rgb color code
BLUE = 0,0,255
RED = 255,0,0


circle_x = 50
circle_y = 50
radius = 50

SPEED_X = 0.5
SPEED_Y = 0.5

while True:

    eventList = pygame.event.get()
    for event in eventList:
        # print(event)
        if event.type == pygame.QUIT:
            # quit the pygame
            pygame.quit()
           # quit the python
            quit()
    SCREEN.fill(WHITE)

    pygame.draw.circle(SCREEN, BLUE, [circle_x, circle_y], radius)
    circle_x += SPEED_X
    circle_y += SPEED_Y

    if circle_x > WIDTH - radius:
        SPEED_X = -0.5
    elif circle_y > HEIGHT - radius:
        SPEED_Y = -0.5
    elif circle_x < radius:
        SPEED_X = 0.5
    elif circle_y < radius:
        SPEED_Y = 0.5




   # update the screen
    pygame.display.flip()
