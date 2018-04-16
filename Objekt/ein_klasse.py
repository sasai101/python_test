# eine Katze
class Katze:
	"""ein Katze definiert"""
	# Attribute
	# Initialisierung des Objekt
	def __init__(self,new_name, new_age):
		#print("---haha---")
		self.name = new_name
		self.age = new_age

	def __str__(self):
		return "Alt von %s ist %d"%(self.name, self.age)
	#Funtkion
	def eat(self):
		print("Katze isst gerade einen Fisch")

	def trink(self):
		print("Katze drinkt gerade Milch")

	def vorstellen(self):
		#print("%s ist schon %s alt"%(tom.name, tom.age))
		print("%s ist schon %s alt"%(self.name, self.age))

# ein Objekt stellen
tom = Katze("Tom", 40)
#ruf die Funtion von Katze
tom.eat()
tom.trink()
#2 Attribute fuer Katze
#tom.name = "Tom"
#tom.age = 40
tom.vorstellen() # ist gleich , tom.vorstellen(tom)
#print("%s ist schon %s alt"%(tom.name, tom.age))

blueCat = Katze("blue cat",10)
#blueCat.name = "blue cat"
#blueCat.age = 20
blueCat.vorstellen()

print(tom)
print(blueCat)
