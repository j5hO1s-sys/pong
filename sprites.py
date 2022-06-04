import pygame
import random


class Player:
    def __init__(self, screen):
        self.screen = screen
        self.resolution = screen.get_size()
        self.x, self.y = (self.resolution[0]*0.8, self.resolution[1]*0.4)
        self.color = (255, 255, 255)
        self.width = 5
        self.height = self.resolution[1]/5
        self.speed = 5
    
    def move_up(self):
        if self.y > 0:
            self.y -= self.speed
    
    def move_down(self):
        if self.y + self.height < self.resolution[1]:
            self.y += self.speed
    
    def draw(self):
        self.sprite = pygame.draw.line(self.screen, self.color, (self.x, self.y), (self.x, self.y+self.height), self.width)
    
    def has_colide(self, h):
        return self.sprite.colliderect(h)



class Ball:
    def __init__(self, screen):
        self.screen = screen
        self.resolution = self.screen.get_size()
        self.x, self.y = (self.resolution[0]*0.1, self.resolution[1]*(random.randint(1, 9)/10))
        self.width, self.height = (10, 10)
        self.color = (255, 0, 0)
        self.speed = 5
        self.gameover = False
        self.reached_border = False
        

        # movements
        self.top = False
        self.bottom = True
        self.left = False
        self.right = True


        self.sprite = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        if self.top:
            self.y -= self.speed
        if self.bottom:
            self.y += self.speed
        if self.left:
            self.x -= self.speed
        if self.right:
            self.x += self.speed



    def draw(self):
        contact = False

        if self.x >= self.resolution[0]:
            self.gameover = True
        
        if self.x <= 0:
            self.left = False
            self.right = True
            contact = True
        
        if self.y >= self.resolution[1]:
            self.top = True
            self.bottom = False
            contact = True

        if self.y <= 0:
            self.top = False
            self.bottom = True
            contact = True
        
        if contact:
            self.reached_border = True
        else:
            self.reached_border = False


        self.move()
        self.sprite = pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
    
    def colision(self):
        if self.left:
            self.left = False
        else:
            self.left = True
        
        if self.right:
            self.right = False
        else:
            self.right = True
        
        