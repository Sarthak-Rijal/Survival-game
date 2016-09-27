import pygame,sys
from tileC import Tile
from object_classes import *

class Bullet(pygame.Rect):
	
	List = []
	
	def __init__(self,x,y,vel_x, vel_y,direction,width,height):
		self.x = x
		self.width = width
		self.height = height
		self.y = y
		self.vel_x = vel_x
		self.vel_y = vel_y
		self.direction = direction
		self.dmg = 50
		
		if self.direction == 'up':
			self.vel_x = vel_x
			self.vel_y = -vel_y
		if self.direction == 'down':
			self.vel_x = vel_x
			self.vel_y = vel_y
		if self.direction == 'left':
			self.vel_x = -vel_x
			self.vel_y = vel_y
		if self.direction == 'right':
			self.vel_x = vel_x
			self.vel_y = vel_y
			
		pygame.Rect.__init__(self, (x,y) ,(self.width,self.height) ) 
		#pygame.Rect.__init__(self, (x, y) , (Tile.width, Tile.height) )
		Bullet.List.append(self)
		
	@staticmethod
	def Bullet_loop(screen):
		for bullet in Bullet.List:
			
			bullet.x += bullet.vel_x
			bullet.y += bullet.vel_y
			
			pygame.draw.rect(screen, (255,0,0), (bullet.x,bullet.y,bullet.width,bullet.height))
			
			if ((bullet.x < 0 or bullet.x > 704) and (bullet.y < 0 or bullet.y>448)):
				Bullet.List.remove(bullet)
				continue
				
			for tile in Tile.List:
				if bullet.colliderect(tile) and not(tile.walkable):
					try:
						Bullet.List.remove(bullet)
					except:
						break
			for goo in Zombie.List:
				if bullet.colliderect(goo):
					goo.health -= bullet.dmg
					Bullet.List.remove(bullet)
					break
					
		
		
		
		
		
		
		
			
		