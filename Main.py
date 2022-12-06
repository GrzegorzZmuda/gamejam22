import pygame
import numpy as np
import pygame.surfarray as sfr
import time
import random
import math
from sys import exit

class wall:
    def __init__(self,x=0,y=700,dir=0):
        self.x=x
        self.y=y
        self.dir=dir
        self.color = (255, 100, 100)
        self.surf = pygame.Surface((470, 20), pygame.SRCALPHA)
        self.rect = pygame.Surface.get_rect(self.surf)

    def mov(self):
        self.rect_update()




    def rect_update(self):
        self.rect = pygame.Surface.get_rect(self.surf,center=(self.x, self.y))
        self.surf.fill(self.color)
        screen.blit(pygame.transform.rotate(self.surf, self.dir),(self.x,self.y))


class hitter:
    def __init__(self):
        self.x=500
        self.y=700
        self.dir=180
        self.color = (100, 255, 100)
        self.surf = pygame.Surface((100, 20), pygame.SRCALPHA)
        self.rect =  pygame.Surface.get_rect(self.surf)

    def mov(self):
        self.rect_update()



    def rect_update(self):
        self.rect = pygame.Surface.get_rect(self.surf,center=(self.x, self.y))
        self.surf.fill(self.color)
        screen.blit(pygame.transform.rotate(self.surf, self.dir),(self.x,self.y))



class ball:
    def __init__(self):
        self.x=395
        self.y=400
        self.dir=270
        self.spd=1
        self.color=(255,255,255)
        self.cld=0
        self.rect = pygame.draw.circle(screen, self.color, (self.x,self.y), 10)

    def grav(self):
        a=self.spd*math.sin(math.radians(self.dir+270))
        b=self.spd*math.sin(math.radians(self.dir+180))


        b=b+0.1

        c=math.sqrt(a*a+b*b)
        self.spd=c
        self.dir=270-math.atan(a/b)*360/(2*3.14)




    def mov(self):
        self.rect_update()
        if self.dir>360:
            self.dir-=360
        if self.dir < 0:
            self.dir += 360
        if  self.y<0:
            self.dirchange()
        if self.x < 0 or self.x > 800:
            self.dirchange2()
        self.x+=self.spd*math.sin(math.radians(self.dir+270))
        self.y+=self.spd*math.sin(math.radians(self.dir+180))
        self.grav()
        print(self.spd)
        print(self.dir)


    def coltest(self, sprite):
        self.cld-=1
        if  self.rect.colliderect(sprite.rect) and self.cld<1:
            self.spd=-self.spd
            self.dir=self.dir+10-random.randrange(0,21)
            self.cld=10





    def rect_update(self):
        self.rect = pygame.draw.circle(screen, self.color, (self.x,self.y), 10)

    def disp(self):
        pygame.draw.circle(screen, self.color, (self.x,self.y), 10)







pygame.init()
screen = pygame.display.set_mode((800,800))
surf1=pygame.surfarray.make_surface(np.full((800,800,3),(50,50,50)))
font = pygame.font.Font('freesansbold.ttf', 20)
Running=True

bl=ball()
hl=hitter()
wl=wall()
wll=wall(600,700,0)

while Running:
    screen.blit(surf1, (0, 0))
    bl.mov()
    hl.mov()
    wl.mov()
    wll.mov()

    bl.coltest(wl)
    bl.coltest(wll)
    bl.coltest(hl)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.flip()
    time.sleep(1)
