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
