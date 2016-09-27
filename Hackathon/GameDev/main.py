import time
import pygame, sys, Funk
from tileC import Tile
from object_classes import *
from interaction import interaction
from A_Star import A_Star
from bullets import *
from random import*


pygame.init()
pygame.font.init()

width = 704
height = 448
screen = pygame.display.set_mode((704, 448)) # 32, 32
image = pygame.image.load('image/ammo_1.png')


    
def print_f(msg,siz,color,x,y):
    Text = pygame.font.Font("freesansbold.ttf",siz)
    write = Text.render(msg,True,color)
    write_rect = write.get_rect()
    write_rect.center = ((x),(y))
    screen.blit(write,write_rect)
    
def lose():
    screen.fill((138,7,7))
    print_f("YOU DIED",32,(0,0,0),width/2,height/2)
    
   


for y in range(0, screen.get_height(), 32):
    for x in range(0, screen.get_width(), 32):
        if Tile.total_tiles in Tile.invalids:
            Tile(x, y, 'solid')
        else:
            Tile(x, y, 'empty')

clock = pygame.time.Clock()
FPS = 20


def main(): 
    total_frames = 0

    survivor = Survivor(32 * 1, 32 * 8,100,'sound/zap.wav',100)
    img = pygame.image.load('image/map.jpg')


    
    while True:
        screen.blit(img,(0,0))
        Zombie.spawn(total_frames, FPS)
        Zombie.movement()

        survivor.movement()

        Bullet.Bullet_loop(screen)

        A_Star(screen, survivor, total_frames, FPS)
        interaction(screen, survivor)
        Tile.draw_tiles(screen)
        survivor.draw(screen)
        Zombie.draw_zombies(screen)
        string_health = str(survivor.health)
        
     
            
        print_f('Health:'+str(survivor.health)+'%',15,(255,0,0),55,25)  #health
        print_f('Ammo:'+str(survivor.ammo), 15,(255,255,255), 650,25) #ammo
        if survivor.health <= 0:
            lose()

        pygame.display.flip()
        clock.tick(FPS)
        total_frames += 1
        
main()
