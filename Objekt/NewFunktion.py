class Dog(object):
	def __init__(self):
		print("_______init________")
	
	def __del__(self):  # shan chu dui xiang de fang fa
		print("_______del________")

	def __str__(self):
		print("_______str________")
		return "Aufzeichnung von duixiang"

	def __new__(cls):  #chuang jian dui xiang de fang fa
		#print(id(cls))
		print("-------new--------")
		return object.__new__(cls)

#print(id(Dog))
dog = Dog()
