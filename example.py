import pygame
import random
pygame.init()

screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
run = True

to_show = []
time = -1

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill((0,0,255))
    for thing in to_show:
        screen.blit(thing,(100,100))
    if to_show == []:
        if random.randint(1,300) == 1:
            to_show.append(pygame.image.load("banaa.png"))
            time = 300
    if not to_show == []:
        time = time -1
        if time < 1:
            to_show = []
    pygame.display.flip()
    clock.tick(60)
pygame.quit()