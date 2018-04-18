class Base(object):  # Objekt-Klasse ist am hoechsten Klasse
	def test(self):
		print("---Base")

class A(Base):
	def test(self):
		print("------A")

class B(Base):
	def test(self):
		print("------B")

class C(B,A):

	def test(self):
		print("------C")
	
		B.test(self)
		A.test(self)
		Base.test(self)
		super().test()

c = C()
c.test()
#c.test1()
#c.test2()
print(c.__mro__)
