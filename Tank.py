import pygame
import math

class Tank:
    
    def __init__(self,x,y,width, height, image, speed, angle = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.speed = speed
        self.angle = angle
        
    def display(self,screen):
        screen.blit(pygame.transform.rotate(self.image,self.angle),
                    (self.x,self.y))
        
    def update(self):
        self.rotate()
        self.back_and_forward()
        
    def rotate(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
          self.angle = self.angle +1  
        if keys[pygame.K_d]:
            self.angle = self.angle -1

        
    def back_and_forward(self):
        keys = pygame.key.get_pressed()
        x = math.sin(math.radians(self.angle))*self.speed
        y = math.cos(math.radians(self.angle))*self.speed
        if keys[pygame.K_w]:
            self.x = self.x - x
            self.y = self.y - y
        if keys[pygame.K_s]:
            self.x = self.x + x
            self.y = self.y + y
        
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)
        
        