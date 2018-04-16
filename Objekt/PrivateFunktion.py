
class Dog:
	
	#private Funtion
	def __send_msg(self):
		print("--------zhengzai fasong--------")

	#public Funktion
	def send_msg(self, new_money):
		if new_money>10000:
			self.__send_msg()
		else:
			print("yuhebuzu")

dog = Dog()
dog.send_msg(100000000)
dog.send_msg(1)

#setter and getter
class Cat:

	#def __init__(self,new_age):
	#	self.age = new_age

	def set_age(self,new_age):
		if new_age>0:
			self.age = new_age
		else:
			self.age = 0
	
	def get_age(self):
		return self.age

cat = Cat()
cat.set_age(10)
print(cat.get_age())
