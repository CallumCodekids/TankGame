import pygame
from Tank import Tank

pygame.init()
clock = pygame.time.Clock()
screen_width = 1000
screen_height = 600
fps = 60
screen = pygame.display.set_mode((screen_width,screen_height))
tank = Tank(400,200,60,60,"player_tank.png", 5, screen)
bg = pygame.image.load("background.jpg")
bg= pygame.transform.scale(bg,(screen_width,screen_height))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(bg,(0,0))
    tank.update()
    tank.display()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()