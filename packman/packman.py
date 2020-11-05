import pygame
import random
pygame.init()
screen = pygame.display.set_mode((612,612))

playerImage = pygame.image.load("player.png")
player_x = 306
player_y = 550

enemyImage = pygame.image.load("enemy.png")
enemy_x = random.randint(100,512)
enemy_y = random.randint(20,50)
enemy_dx = 5
enemy_dy = 50

bulletImage = pygame.image.load("bullet.png")
bullet_x = 314
bullet_y = 594  

backgroundImage = pygame.image.load("background.jpg")

def player(x,y):
    screen.blit(playerImage,(x,y))

def enemy(x,y):
    screen.blit(enemyImage,(x,y))

def bullet(x,y):
    screen.blit(bulletImage,(x,y))
score = 0

def drawScore():
    global score
    font = pygame.font.SysFont('smaller.fon', 30)
    text = font.render(f'Score:{score}', 1, (0, 0, 0))
    screen.blit(text, (530, 40))

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            player_x = player_x-5
            bullet_x = bullet_x-5
        if event.key == pygame.K_RIGHT:
            player_x = player_x+5
            bullet_x = bullet_x+5
        if event.key == pygame.K_SPACE:
            if bullet_y < 0:
                bullet_y += 600
            bullet_y-=5
    dist_x = bullet_x - enemy_x
    dist_y = bullet_y - enemy_y
    
    if -24 <= dist_x <= 64 and -24 <= dist_y <= 64 :
        bullet_x, bullet_y = 306, 586
        enemy_x, enemy_y = random.randint(100,512), random.randint(20, 50)
        score+=1

    screen.fill((0,0,0))    
    screen.blit(backgroundImage,(0,0))
    drawScore()
    player(player_x,player_y)
    bullet(bullet_x,bullet_y)
    enemy_x+=enemy_dx
    if enemy_x<0 or enemy_x>612:
        enemy_dx = -enemy_dx
        enemy_y += enemy_dy
    if enemy_y > 612:
        enemy_y -=570
    enemy(enemy_x,enemy_y)
    pygame.display.flip()  