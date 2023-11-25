import pygame
import random
from Tank import Tank
from Collectables import Collectables
from breakable_blocks import Breakable_Blocks
pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 600
fps = 60
breakblocks = [Breakable_Blocks(100,100,60,60,"breakable block.png", 3), Breakable_Blocks(100,160,60,60,"breakable block.png", 3)]
screen = pygame.display.set_mode((screen_width,screen_height))
tank = Tank(400,200,60,60,"player_tank.png", 5, screen)
bg = pygame.image.load("background.jpg")
bg= pygame.transform.scale(bg,(screen_width,screen_height))
collect = 0
power_up = False
amount = 10
run = True
collectables = []
power_up_last = 0
power_up = False
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(bg,(0,0))
    tank.update()      
    tank.display()
    tank_rect = tank.get_rect()
    for block in breakblocks:
        breakable_blocks_rect = block.get_rect()
        if tank_rect.colliderect(breakable_blocks_rect):
            print("collide")
        block.display(screen)
    for collectable in collectables:
        collectable_rect = collectable.get_rect()
        if tank_rect.colliderect(collectable_rect):
            collectables.remove(collectable)
            tank = Tank(tank.x,tank.y,100,100,"power up tank.png", 7, screen, tank.angle)
            power_up = True
        collectable.display(screen)
    if collect > amount:
        collectables.append(Collectables(random.randrange(100,screen_width),random.randrange(100,screen_height),180,160,"fire ball.png",7))
        collect = 0
    collect += 0.01
    if power_up == True:
        power_up_last += 0.01
    if power_up_last >= 10:
        power_up = False
        tank = Tank(tank.x,tank.y,40,40,"player_tank.png", 5, screen, tank.angle)
        power_up_last = 0
    tank.display()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()