import pygame
import time
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
		for emmotion in self.emmotion_list:
			emmotion.display()
	
	def move_left(self):
		self.x -= 5

	def move_right(self):
		self.x += 5

	def feuer(self):
		self.emmotion_list.append(Emmotion(self.screen)

class Emmotion(object):
	def __init__(self,screen_temp):
		self.x = 0 
		self.y = 0
		self.zidan = pygame.image.load("./Downloads/zidan01.png")
		self.screen = screen_temp

	def display(self):
		self.screen.blit(self.zidan,(self.x,self.y))

def kontr(wo):
	for event in pygame.event.get():

		if event.type ==QUIT:
			print("exit")
			exit()
		elif event.type == KEYDOWN:
			if event.key == K_LEFT:
				wo.move_left()
				print("left")
			elif event.key == K_RIGHT:
				wo.move_right()
				print("right")
			elif event.key == K_SPACE:
				print("space")

def main():
	
	#1, Hauptwindows
	screen = pygame.display.set_mode((480,852),0,32)

	#2, Hintergrund erstellen
	hintergrund = pygame.image.load("./Downloads/beijing.png")

	#3 eine Flug erstellen
	wo = Wo(screen)

	#3 Hintergrund anzeigen
	while True:
		screen.blit(hintergrund,(0,0))
		wo.display()
		
		#in der Monitur anzeigen
		pygame.display.update()
		kontr(wo)
		#pro 0.01s ein mal aktualisieren
		time.sleep(0.01)
		
if __name__ == "__main__":
	main()
