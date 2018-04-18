class CarStore(object):

	def __init__(self):
		self.factory = Factory()

	def order(self,car_type):
		return self.factory.select_cartype(car_type)

class Factory(object):
	def select_cartype(self,car_type):
		if car_type=="Suo":
			# xxxx = Car() # genau gleich wie return Car()
			return Suonata()
		elif car_type=="Min":
			return Mingtu()
		elif car_type=="Ix":
			return Ix35()

class Car(object):
	def move(self):
		print("----move----")
	def stop(self):
		print("----stop----")

class Suonata(Car):
	pass

class Mingtu(Car):
	pass

class Ix35(Car):
	pass

car_store = CarStore()

car = car_store.order("Suo")
car.move()
car.stop()

car = car_store.order("Min")
car.move()
car.stop()

car = car_store.order("Ix")
car.move()
car.stop()
