import pygame
import time
import random
from pygame.locals import *

class Wo(object):
	
	def __init__(self,screen_temp):
		self.x = 200
		self.y = 660
		self.wo = pygame.image.load("./Downloads/wo02.png")
		self.screen = screen_temp
		self.emmotion_list = []

	def display(self):
		self.screen.blit(self.wo,(self.x,self.y))

		for zidan in self.emmotion_list:
			zidan.display()
			zidan.move()
			if zidan.zidan_yuejie():
				self.emmotion_list.remove(zidan)
	
	def move_left(self):
		self.x -= 5

	def move_right(self):
		self.x += 5

	def move_up(self):
		self.y -= 5

	def move_down(self):
		self.y += 5

	def feuer(self):
		self.emmotion_list.append(Zidan01(self.screen,self.x,self.y))
		
class Diji01(object):

	def __init__(self,screen_temp):
		self.x = random.randint(0,450)
		self.y = 0
		self.wo = pygame.image.load("./Downloads/diji01.png")
		self.screen = screen_temp
		#self.emmotion_list = []

	def display(self):
		self.screen.blit(self.wo,(self.x,self.y))

	def move(self):
		self.y += random.randint(5,10)

		#for zidan in self.emmotion_list:
		#	zidan.display()
		#	zidan.move()
	

	#def feuer(self):
	#	self.emmotion_list.append(Zidan01(self.screen,self.x,self.y))

class Diji02(Diji01):
	def __init__(self,screen_temp):
		self.x = random.randint(0,450)
		self.y = 0
		self.screen = screen_temp
		self.wo = pygame.image.load("./Downloads/2diji01.png")


class Zidan01(object):

	def __init__(self,screen_temp,x_temp,y_temp):
		self.x = x_temp + 45
		self.y = y_temp - 20
		self.screen = screen_temp
		self.zidan01 = pygame.image.load("./Downloads/zidan01.png")

	def display(self):
		self.screen.blit(self.zidan01,(self.x,self.y))

	def move(self):
		self.y -= 15

	def zidan_yuejie(self):
		if self.y<0:
			return True
		else:
			return False

def kontr(wo_temp):
	for event in pygame.event.get():

		if event.type ==QUIT:
			print("exit")
			exit()
		elif event.type == KEYDOWN:
			if event.key == K_LEFT:
				wo_temp.move_left()
				print("left")
			elif event.key == K_RIGHT:
				wo_temp.move_right()
				print("right")
			elif event.key == K_SPACE:
				wo_temp.feuer()
				print("space")
			elif event.key == K_UP:
				wo_temp.move_up()
				print("up")
			elif event.key == K_DOWN:
				wo_temp.move_down()
				print("down")

def main():
	
	#1, Hauptwindows
	screen = pygame.display.set_mode((480,852),0,32)

	#2, Hintergrund erstellen
	hintergrund = pygame.image.load("./Downloads/beijing.png")

	#3 eine Flug erstellen
	wo = Wo(screen)
	pan = False

	pan2 = False

	if random.randint(1,5) == 3:
		diji = Diji01(screen)
		pan = True
		
	if random.randint(1,5) == 3:
		diji01 = Diji02(screen)
		pan2 = True

	#3 Hintergrund anzeigen
	while True:
		screen.blit(hintergrund,(0,0))
		wo.display()
		if pan == True:
			diji.display()
			diji.move()
		if pan2 == True:
			diji01.display()
			diji01.move()

		#in der Monitur anzeigen
		pygame.display.update()
		kontr(wo)
		#pro 0.01s ein mal aktualisieren
		time.sleep(0.01)
		
if __name__ == "__main__":
	main()
