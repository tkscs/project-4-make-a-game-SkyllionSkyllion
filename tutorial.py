import pygame
from pygame.locals import *
import sys
import random
import time
import abc
from ido import *



# object1 = pygame.Rect((20,50), (50,100))
# object2 = pygame.Rect((10,10),(100,100))
# print(object1.colliderect(object2))
# print(object1.collidepoint(50,75))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top>0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0,-5)
        if self.rect.bottom<SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                    self.rect.move_ip(-5,0)
        if self.rect.right <SCREEN_WIDTH:       
            if pressed_keys[K_RIGHT]:
                    self.rect.move_ip(5,0)

    def draw(self,surface):
            surface.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
      def move(self):
            self.rect.move_ip(0,SPEED)
            if (self.rect.top>600):
                self.rect.top = 0
                self.rect.center = (random.randint(30,SCREEN_WIDTH-40),0)
      def draw(self,surface):
            surface.blit(self.image,self.rect)

P1 = Player()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)


while True:
     main_loop()