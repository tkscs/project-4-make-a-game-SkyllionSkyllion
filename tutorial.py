import pygame
from pygame.locals import *
import sys
import random
import time
from utils import *
import utils



INC_GAMETIME = pygame.USEREVENT + 2
game_timer = 0
pygame.init()
pygame.display.init()
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(white)
pygame.display.set_caption("Game")
pointcounter = 0


INC_SPEED = pygame.USEREVENT + 1

class Enemy(pygame.sprite.Sprite):
    global game_timer
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.image = pygame.transform.scale_by(self.image, 0.1)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)
        self.active = True
        self.respawn_timer = 0

    def move(self):
            # current_time = pygame.time.get_ticks()
            if not self.active:
                if pygame.time.get_ticks() >= self.respawn_timer:
                    self.active = True
                    self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
                return
            self.rect.move_ip(0,utils.SPEED)
            if (self.rect.top>SCREEN_HEIGHT):
                self.spawn()
                pygame.event.post(pygame.event.Event(INC_SPEED))
            if game_timer>30:
                 self.active = False
                 self.kill()

    
    def spawn(self):
                
                self.active = False
                delay = (2000/(game_timer+1)*random.uniform(1,3))
                self.respawn_timer = pygame.time.get_ticks() + delay
    def draw(self,surface):
            surface.blit(self.image,self.rect)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.image = pygame.transform.scale_by(self.image, 0.5)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2,520)
        self.active = True
        self.player_height = 520 
        self.player_sideways = SCREEN_WIDTH/2
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.top>0:
            if pressed_keys[K_UP]:
                self.rect.move_ip(0,-5)
                self.player_height += - 5
        if self.rect.bottom<SCREEN_HEIGHT:
            if pressed_keys[K_DOWN]:
                self.rect.move_ip(0,5)
                self.player_height += 5
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
                self.player_sideways += -5
        if self.rect.right <SCREEN_WIDTH:       
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)
                self.player_sideways += 5



    def draw(self,surface):
            surface.blit(self.image, self.rect)

class Projectile(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Projectile.png")
        self.image = pygame.transform.scale_by(self.image, .3)
        self.rect = self.image.get_rect()
        self.rect.center = (P1.player_height, P1.player_sideways)
        self.active = False
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_SPACE]:
            self.rect.center = (P1.player_sideways, P1.player_height)
            self.active = True
        self.rect.move_ip(0, -15)
        
class Finalboss(pygame.sprite.Sprite):
    global game_timer
    def __init__(self):
          super().__init__()
          self.image = pygame.image.load("Finalboss.png")
          self.image = pygame.transform.scale_by(self.image, 2)
          self.rect = self.image.get_rect()
          self.active = False
    def move(self):
        if self.active == False:
            if game_timer > 30:
                self.actve = True
                self.rect.center = (SCREEN_WIDTH/2,0)
                sidemove = random.randint(-10,10)
        else:
            self.rect.move_ip(random.randint(sidemove-10, sidemove+10),((utils.SPEED)/2))
            
         
    

#POINT SYSTEM





#NEW CLASS OF PROJECTILE
#PROJECTILE COLLISION WITH ENEMIES



P1 = Player()
E1 = Enemy()
E2 = Enemy()
E3 = Enemy()
E4 = Enemy()
E5 = Enemy()
E6 = Enemy()
E7 = Enemy()
E8 = Enemy()
E9 = Enemy()
E10 = Enemy()
PJ1 = Projectile()
FB1 = Finalboss()

enemies = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemies.add(E1, E2, E3, E4, E5, E6, E7, E8, E9, E10)
finalboss = pygame.sprite.Group()
finalboss.add(FB1)
projectiles.add(PJ1)


all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1, E2, E3, E4, E5, E6, E7, E8, E9, E10)
all_sprites.add(PJ1)
all_sprites.add(FB1)



# pygame.time.set_timer(INC_SPEED, 1000)
pygame.time.set_timer(INC_GAMETIME, 1000)
def main_loop():
    global pointcounter
    global game_timer
    for event in pygame.event.get():
        # print (event)
        if event.type == INC_GAMETIME:
             game_timer += 1
        if event.type == INC_SPEED:
            utils.SPEED +=.02
            
            # print(utils.SPEED)
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(white)
    for entity in all_sprites:
        entity.move()
        if entity.active:
            DISPLAYSURF.blit(entity.image, entity.rect)
    if pygame.sprite.spritecollideany(P1, enemies):
        DISPLAYSURF.fill(red)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        print(f"You survived for {game_timer} seconds. You shot {pointcounter} Keo's with fireballs")
        sys.exit()
    projectilehit = pygame.sprite.spritecollideany(PJ1, enemies)
    if projectilehit !=  None:
        print(f"{projectilehit =}")
        projectilehit.spawn()
        PJ1.rect.center = (-1000,-1000)
        pointcounter += 1



        
        



    pygame.display.update()
    FramePerSec.tick(FPS)


while True:
    main_loop()