import sys
#__del__

class Dog:
	
	def __del__(self):  # Wenn das Klass zum Ende ist, dann wird __del__ Funktion automatisch rufen.
		print("die Figur ist tot!!")

dog1 = Dog()
dog2 = dog1

print(sys.getrefcount(dog1))

del dog2

print(sys.getrefcount(dog1))

#del dog2
print("=======================")
