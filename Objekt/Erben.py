#Erben

class Animal:
	def eat(self):
		print("-----essen-----")
	def drinken(self):
		print("-----drink-----")
	def laufen(self):
		print("-----laufen-----")
	def schlafen(self):
		print("-----schlafen-----")

class Dog(Animal):
	def bark(self):
		print("------wang wang wang------")

class Cat(Animal):
	def catch(self):
		print("-----zhua lao shu-------")

class Xiaotianquan(Dog):
	def fliegen(self):
		print("-------kann fliegen-------")
	def bark(self):
		print("------ziemlich schreien")
		
		#1. Altenativ um die Funktion von Vaterklasse zu rufen
		#Dog.bark(self)

		#2. Altenativ um die Funktion von Vaterklasse zu rufen
		super().bark()


wangcai = Dog()
wangcai.eat()
wangcai.bark()
print("==========================")
tom = Cat()
tom.eat()
tom.catch()
tom.schlafen()
print("==========================")
xiao = Xiaotianquan()
xiao.fliegen()
xiao.bark()
xiao.eat()
