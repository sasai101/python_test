class Home:
	def __init__(self,new_area, new_info, new_addr):
		self.area = new_area
		self.info = new_info
		self.addr = new_addr
		self.left = new_area
		self.contain_item = []

	def __str__(self):
		msg = "Grundstueck: %d  Zimmeranzahl: %d Addresse: %s nochfreie Flache: %d"%(self.area, self.info, self.addr, self.left)
		msg += " Es gibt ein %s in zimmer "%(str(self.contain_item))
		return msg
	
	def add_item(self,item):
		#self.left -= item.gross
		#self.contain_item.append(item.name)

		self.left -= item.get_gross()
		self.contain_item.append(item.get_name())

class Bett:
	def __init__(self, new_name, new_gross):
		self.name = new_name
		self.gross = new_gross
	def __str__(self):
		return "%s hat %d gross"%(self.name, self.gross)
	
	def get_name(self):
		return self.name
	def get_gross(self):
		return self.gross
	
fangzi = Home(129,3,"Koln")
print(fangzi)

bett1 = Bett("ximengsi", 4)
print(bett1)

fangzi.add_item(bett1)
print(fangzi)

bett2 = Bett("sanrenchuang",6)

fangzi.add_item(bett2)
print(fangzi)
