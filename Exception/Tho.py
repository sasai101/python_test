class Test(object):
	def __init__(self, switch):
		self.switch = switch
	
	def calc(self,a,b):
		try:
			return a/b
		except Exception as result:
			if self.switch:
				print("ein Fehler gefunden, Fehlertyp ist :")
				print(result)
			else:
				raise

a = Test(True)
a.calc(11,0)

print("---------------------------------------------")

a.switch = False
a.calc(11,0)
