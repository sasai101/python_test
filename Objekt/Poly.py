class Dog(object):
	def print_self(self):
		print("hallo,ich freue mich hier zu sein!")

class Xiaotianq(Dog):
	def print_self(self):
		print("hello everybody, i am the boss")

def vorstellen(temp):
	temp.print_self()

dog1 = Dog()
dog2 = Xiaotianq()

vorstellen(dog1)
vorstellen(dog2)
