import pygame

class Tank:
    
    def __init__(self,x,y,width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image,(self.width,self.height))
        self.speed = 0
        self.angle = 0
        
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
        if keys[pygame.K_w]:
          self.y = self.y -1  
        if keys[pygame.K_s]:
            self.y = self.y +1
        