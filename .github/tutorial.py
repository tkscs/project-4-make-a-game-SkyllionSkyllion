import pygame
from pygame.locals import *
import sys
import random
import time

pygame.init()


black = pygame.Color(0,0,0) #Black
white = pygame.Color(255,255,255) #White
gray = pygame.Color(128,128,128) #Gray
red = pygame.Color(255,0,0) #Red


SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 750
SPEED = 5
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(white)
pygame.display.set_caption("Game")







FPS = 60
FramePerSec = pygame.time.Clock()

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

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
             SPEED +=2
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(white)
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(red)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit



    pygame.display.update()
    FramePerSec.tick(FPS)