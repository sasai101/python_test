import pygame
import time
from pygame.locals import *
import random

class Flug(object):
	"""Vater Klasse von alle Flug"""
	def __init__(self,fenster,x,y,image_name,leben):
		self.x = x
		self.y = y
		self.fenster = fenster
		self.Flug = pygame.image.load(image_name)
		self.leben = leben

class Mein_Flug(Flug):
	"""Mein Flug einzeigen und kontorlieren"""
	def __init__(self, fenster):
		Flug.__init__(self,fenster,200,600,"./Downloads/wo02.png",1)
		self.image = [pygame.image.load("./Downloads/wo03.png"),pygame.image.load("./Downloads/wo04.png"),pygame.image.load("./Downloads/wo05.png"),pygame.image.load("./Downloads/wo06.png")]
		self.emmotion_list = []

	# Flug anzeigen
	def anzeigen(self):
		self.fenster.blit(self.Flug,(self.x, self.y))
		#Emmotion anzeigen, sich bewehgen, loeschen, wenn es uebergrenze fliegt
		for emmotion in self.emmotion_list:
			emmotion.emmotion_anzeigen()
			emmotion.move()
			if emmotion.emmotion_uber_grenz():
				self.emmotion_list.remove(emmotion)
		
	# geht nach links
	def move_link(self):
		self.x -= 3

	# geht nacht rechts
	def move_recht(self):
		self.x += 3

	def move_oben(self):
		self.y -= 3

	def move_unten(self):
		self.y += 3
		
	def feuer(self):
		# die Emmotion, die meinen Flug geschsossen haben, in der list einspeichern
		self.emmotion_list.append(Emmotion(self.fenster,self.x,self.y))

	# Getter von List der Emmotion
	def get_emmotionList(self):
		return self.emmotion_list

	# Getter von der Position
	def get_position_x(self):
		return self.x 
	
	def get_position_y(self):
		return self.y	

class Emmotion(object):
	"""Emmotionsinformation"""
	def __init__(self,fenster,x_temp,y_temp):
		self.x = x_temp + 45
		self.y = y_temp - 20
		self.fenster = fenster
		self.emmotion = pygame.image.load("./Downloads/zidan01.png")

	# wird in der Mein_Flug Klasse gerufen
	def emmotion_anzeigen(self):
		self.fenster.blit(self.emmotion,(self.x,self.y))

	def move(self):
		self.y -= 15

	def emmotion_uber_grenz(self):
		if self.y < 0:
			return True
		else:
			return False

class Feind_Flug(Flug):
	"""Vater Klasse von alle Feindfluegen"""
	def __init__(self,fenster,x,y,image_name,move_geschwindigkeit,leben):
		Flug.__init__(self,fenster,x,y,image_name,leben)
		self.geschwindigkeit = move_geschwindigkeit

	def feind_flug_anzeigen(self):
		self.fenster.blit(self.Flug,(self.x,self.y))

	def feind_move(self):
		self.y += self.geschwindigkeit

	def feind_uebergrenze(self):
		if self.y>852+self.Flug.get_rect().height:
			return True
		else:
			return False

# 3 unterschiedliche Feindfluege
class Feind_Flug1(Feind_Flug):

	def __init__(self,fenster):
		Feind_Flug.__init__(self, fenster, random.randint(0,399),-39,"./Downloads/diji01.png",random.randint(2,5),0)

class Feind_Flug2(Feind_Flug):

	def __init__(self,fenster):
		Feind_Flug.__init__(self, fenster, random.randint(0,381),-89,"./Downloads/2diji01.png",random.randint(2,4),2)
		

class Feind_Flug3(Feind_Flug):

	def __init__(self,fenster):
		Feind_Flug.__init__(self, fenster, random.randint(0,285),-246,"./Downloads/3diji01.png",1,6)

		
class Feind(object):
	"""Feindflug in der List addieren, anzeigen, und loschen wenn die ubergrenze fliegt"""
	def __init__(self,fenster):
		self.fenster = fenster
		self.feind_flug_list = []
	# Feindflug in der List addieren
	def feind_flug_add(self):
		if random.randint(0,70) == 1:
			self.feind_flug_list.append(Feind_Flug1(self.fenster))
		if random.randint(0,300) == 1:
			self.feind_flug_list.append(Feind_Flug2(self.fenster))
		if random.randint(0,800) == 1:
			self.feind_flug_list.append(Feind_Flug3(self.fenster))
	# Feind anzeigen , bewegen und loeschen
	def feind_anzeigen(self):
		for feind in self.feind_flug_list:
			feind.feind_flug_anzeigen()
			feind.feind_move()
			if feind.feind_uebergrenze():
				self.feind_flug_list.remove(feind)
	#Getter von Feindfluege List
	def get_feindfluglist(self):
		return self.feind_flug_list

class Hintergrund(object):
	"""Hintergrund anzeigen und bewegen"""
	def __init__(self,fenster):
		self.x = 0
		self.y = 0
		self.fenster = fenster
		self.hintergrund = pygame.image.load("./Downloads/beijing.png")
	# Hintergrund in der Hauptfenster anzeigen
	def hintergrund_anzeigen(self):
		self.fenster.blit(self.hintergrund,(self.x,self.y))
	
	# laess den Hintergrund in loop
	def hintergrund_move(self):
		
		rel_y = self.y % self.hintergrund.get_rect().height
		#print("OK")
		self.fenster.blit(self.hintergrund,(0,rel_y - self.hintergrund.get_rect().height))
		if rel_y < 852:
			self.fenster.blit(self.hintergrund,(0,rel_y))
		self.y += 1


def kontroller(mein_flug):
	"""dadurch mein Fulg zu kontrolieren"""
	# Nimmt alle Reaktion, was man in Spiel gemacht hat
	for event in pygame.event.get():
		#print("OK")	
		# wenn das Kreuz oben recht druckt, schlatet das Spiel aus
		if event.type == QUIT:
			exit()
		elif event.type == KEYDOWN:
			if event.key == K_SPACE:
				mein_flug.feuer()
				#print("OKOK")
	# Dauerhaft nimmt die Befehler von Tastur
	pressed_keys = pygame.key.get_pressed()
	if pressed_keys[K_LEFT]:
		mein_flug.move_link()
	elif pressed_keys[K_RIGHT]:
		mein_flug.move_recht()
	elif pressed_keys[K_UP]:
		mein_flug.move_oben()
	elif pressed_keys[K_DOWN]:
		mein_flug.move_unten()

# entscheiden, ob die Emmotion die Feindfluege getroffen hat
def feind_wird_geschossen(mein_flug,feind_flug):
	for position in feind_flug.get_feindfluglist():
		#print(position.y)
		for emmotion_position in mein_flug.get_emmotionList():
			if position.x <= emmotion_position.x <= position.x + position.Flug.get_rect().width and position.y<=emmotion_position.y<=position.y +position.Flug.get_rect().height:
				if position.leben == 0:
					mein_flug.emmotion_list.remove(emmotion_position)
					feind_flug.feind_flug_list.remove(position)
				else:
					position.leben -= 1
					mein_flug.emmotion_list.remove(emmotion_position)

# entscheiden, ob die Feindfluege meinen Flug getroffen hat
def meinFlug_wird_gestossen(mein_flug,feind_flug):
	for position in feind_flug.get_feindfluglist():
		if mein_flug.x <= position.x <= mein_flug.x + mein_flug.Flug.get_rect().width or position.x <= mein_flug.x <= position.x + position.Flug.get_rect().width:
			if mein_flug.y <= position.y <= mein_flug.y + mein_flug.Flug.get_rect().height or position.y <= mein_flug.y <= position.y + position.Flug.get_rect().height:
				exit() # wenn getroffen aus
			else:
				pass

def main():
	#print("OK")
	# Hauptwindows ohne Hintergrund
	fenster = pygame.display.set_mode((480,852),0,32)

	# Der Hintergrund auf Hauptwindows einzusetzen
	hintergrund = Hintergrund(fenster)

	# Flug von Spieler
	mein_flug = Mein_Flug(fenster)

	#feind_Flug1 = Feind_Flug1(fenster)
	feind_flug = Feind(fenster)

	# Hintergrund anzuzeigen
	while True:
		# setzt den Hintergrund auf der Postion x = 0 und y = 0
		hintergrund.hintergrund_anzeigen()
		hintergrund.hintergrund_move()
		# mein Flug in der Fenster anzuzeigen
		mein_flug.anzeigen()

		#Feindflug anzuzeigen
		feind_flug.feind_flug_add()
		feind_flug.feind_anzeigen()
		# in der Monitur anzeigen
		pygame.display.update()

		# ruf die Funktion kontroller, um meinen Flug zu kontrollieren
		kontroller(mein_flug)

		feind_wird_geschossen(mein_flug,feind_flug)

		meinFlug_wird_gestossen(mein_flug,feind_flug)

		# Lass die Programm langsam laufen(CPU Problem)
		time.sleep(0.001)

if __name__=="__main__":
	main()