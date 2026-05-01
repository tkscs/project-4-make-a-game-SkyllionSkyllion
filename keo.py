import pygame
from pygame.locals import *
import sys
import random
import time
from utils import *



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