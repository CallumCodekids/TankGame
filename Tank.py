import pygame
import math

class Tank:
    
    def __init__(self,x,y,width, height, image, speed, screen, angle = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.speed = speed
        self.angle = angle
        self.screen = screen
        
    def display(self):
        self.screen.blit(pygame.transform.rotate(self.image,self.angle),
                    (self.x,self.y))
        
    def update(self):
        self.rotate()
        self.back_and_forward()
        self.keep_in_screen()
        
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
            
    def collision(self):
        

    def keep_in_screen(self):
        miny = 0
        minx = 0
        maxy = self.screen.get_height() - self.height
        maxx = self.screen.get_width() - self.width
        if self.x > maxx:
            self.x = maxx
        if self.y > maxy:
            self.y = maxy
        if self.y < miny:
            self.y = miny
        if self.x < minx:
            self.x = minx
        
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)
        
        