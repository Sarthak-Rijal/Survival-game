import pygame, sys
from tileC import Tile
from bullets import *
from object_classes import *

def interaction(screen, survivor):

    Mpos = pygame.mouse.get_pos() # [x, y] 
    Mx = Mpos[0] / Tile.width
    My = Mpos[1] / Tile.height

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            for tile in Tile.List:
                if tile.x == (Mx * Tile.width) and tile.y == (My * Tile.width):
                    tile.type = 'solid'
                    tile.walkable = False
                    break

    
    
    
            
    
    keys = pygame.key.get_pressed()


    if keys[pygame.K_SPACE]:
        
        if survivor.direction == 'up' and survivor.ammo>=0 :
            Bullet(survivor.x,survivor.y,0,25,'up',4,10)
            survivor.zap.play()
            survivor.ammo-=1
        if survivor.direction == 'down'and survivor.ammo>=0:
            Bullet(survivor.x,survivor.y,0,25,'down',4,10)
            survivor.zap.play()
            survivor.ammo-=1
        if survivor.direction == 'left'and survivor.ammo>=0:
            Bullet(survivor.x,survivor.y,25,0,'left',10,4)
            survivor.zap.play()
            survivor.ammo-=1
        if survivor.direction == 'right'and survivor.ammo>=0:
            Bullet(survivor.x,survivor.y,25,0,'right',10,4)
            survivor.zap.play()
            survivor.ammo-=1
    if keys[pygame.K_w] or keys[pygame.K_UP]: # North
        future_tile_number = survivor.get_number() - Tile.V
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                survivor.set_target(future_tile)
                survivor.rotate('up')
                # survivor.y -= survivor.height                   

    if keys[pygame.K_s] or keys[pygame.K_DOWN]: # South
        future_tile_number = survivor.get_number() + Tile.V
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                survivor.set_target(future_tile)
                survivor.rotate('down')
                # survivor.y += survivor.height 

    if keys[pygame.K_a] or keys[pygame.K_LEFT]: # West
        future_tile_number = survivor.get_number() - Tile.H

        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)    
            if future_tile.walkable:
                survivor.set_target(future_tile)
                survivor.rotate('left')
                # survivor.x -= survivor.width 

    if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # East
        future_tile_number = survivor.get_number() + Tile.H
        if future_tile_number in range(1, Tile.total_tiles + 1):
            future_tile = Tile.get_tile(future_tile_number)
            if future_tile.walkable:
                survivor.set_target(future_tile)
                survivor.rotate('right')
                # survivor.x += survivor.width 
    
    number = ((survivor.x/32)+(survivor.y/32)*22)
    for goop in Zombie.List:
        if (goop.colliderect(survivor)):
            survivor.health -= 4
        
            
            
            
            
            
            
            
            
            
           