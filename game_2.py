import pygame
import random
pygame.init() #initialize

SIZE = WIDTH, HEIGHT = 1000, 700
SCREEN = pygame.display.set_mode(SIZE)

WHITE = 255,255,255#rgb color code
BLUE = 0,0,255
RED = 255,0,0
BLACK = 0,0,0

bulletSound = pygame.mixer.Sound("assets/sounds/shoot.wav")
enemySound = pygame.mixer.Sound("assets/sounds/mixkit-flute-alert-2307.wav")

def homeScreen():
    font = pygame.font.Font("assets/fonts/astron boy.otf", 130)
    text = font.render(f"Space Shooter", True, WHITE)

    font_2 = pygame.font.Font("assets/fonts/astron boy wonder.otf", 70)
    text_2 = font_2.render(f"Press SPACE to Start Game", True, WHITE)
    while True:
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()

        SCREEN.blit(text, (130, 200))
        SCREEN.blit(text_2, (80, 350))
        pygame.display.flip()

def playerHealth(count):
    font = pygame.font.SysFont(None, 30)
    text = font.render(f"HEALTH : {count}", True, BLACK)
    SCREEN.blit(text, (10, 500))

def gameOver():
    font = pygame.font.SysFont(None, 80)
    text = font.render(f"GAME OVER", True, RED)
    while True:
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        SCREEN.blit(text, (300, 300))
        pygame.display.flip()

def main ():
    move_x = 0


    ship = pygame.image.load("assets/images/spaceship.1.png")
    ship_w = ship.get_width()
    ship_h = ship.get_height()
    ship_x = WIDTH // 2 - ship_w // 2
    ship_y = HEIGHT - ship_h

    enemyShip = pygame.image.load("assets/images/enemyimage35.png")
    eship_w = enemyShip.get_width()
    eship_h = enemyShip.get_height()

    enemyList = []
    nrow = 3
    ncols = WIDTH // eship_w

    # Bullet Code

    bullet_y = ship_y
    bullet_w = 5
    bullet_h = 10
    moveBullet = 0


    for i in range(nrow):
        for j in range(ncols):
            enemyX = eship_w * j
            enemyY = eship_h * i
            enemyRect =  pygame.Rect(enemyX, enemyY, eship_w, eship_h)
            enemyList.append(enemyRect)
           # enemyList.append([enemyX, enemyY])

    random_enemy = random.choice(enemyList)
    enemy_bullet_w = 5
    enemy_bullet_h = 10
    enemy_bullet_x = random_enemy.x + eship_w//2
    enemy_bullet_y = random_enemy.bottom - 10

    playerHealthCount = 100



    while True:
        bullet_x = ship_x + ship_w // 2 - 2
        eventList = pygame.event.get()
        for event in eventList:
            # print(event)
            if event.type == pygame.QUIT:
                # quit the pygame
                pygame.quit()
               # quit the python
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_x = 2
                elif event.key == pygame.K_LEFT:
                    move_x = -2
                elif event.key == pygame.K_SPACE:
                    moveBullet = -8
                    bulletSound.play()
            else:
                move_x = 0

        SCREEN.fill(WHITE)

        bullet_rect = pygame.draw.rect(SCREEN, RED, [bullet_x, bullet_y, bullet_w, bullet_h])
        bullet_y += moveBullet

        SCREEN.blit(ship, (ship_x, ship_y))
        ship_x += move_x

        ship_rect = pygame.Rect(ship_x, ship_y, ship_w, ship_h)

        enemyBullet = pygame.draw.rect(SCREEN, BLUE, [enemy_bullet_x, enemy_bullet_y, enemy_bullet_w, enemy_bullet_h])
        enemy_bullet_y += 8

        for i in range(len(enemyList)):
           # SCREEN.blit(enemyShip, (enemyList[i][0], enemyList[i][1]))
             SCREEN.blit(enemyShip, (enemyList[i].x, enemyList[i].y))



        for i in range(len(enemyList)):
            if bullet_rect.colliderect(enemyList[i]):
                del enemyList[i]
                bullet_y = ship_y
                moveBullet = 0
                break



        if bullet_y < 0:
            bullet_y = ship_y
            moveBullet = 0

        if enemy_bullet_y > HEIGHT:
            random_enemy = random.choice(enemyList)
            enemy_bullet_x = random_enemy.x + eship_w // 2
            enemy_bullet_y = random_enemy.bottom - 10



        if enemyBullet.colliderect(ship_rect):
            playerHealthCount -= 1
            enemySound.play()


        if playerHealthCount == 0:
            gameOver()



        playerHealth(playerHealthCount)
       # update the screen
        pygame.display.flip()

#main()
homeScreen()


