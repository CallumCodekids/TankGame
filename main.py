import pygame
from Tank import Tank

pygame.init()

screen_width = 1000
screen_height = 600
tank = Tank(400,200,40,60,"player_tank.png")
screen = pygame.display.set_mode((screen_width,screen_height))
bg = pygame.image.load("background.jpg")
bg= pygame.transform.scale(bg,(screen_width,screen_height))

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(bg,(0,0))
    tank.display(screen)
    pygame.display.flip()
            
pygame.quit()