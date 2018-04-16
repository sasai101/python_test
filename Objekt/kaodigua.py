#di gua
class susskatoffel:

	def __init__(self):
		self.kochString = "shengde"
		self.kochLever = 0
		self.zutat = []

	def __str__(self):
		return "diguade zhuangtai :%s(%d). yijiaru %s"%(self.kochString, self.kochLever,str(self.zutat))

	def koch(self, kochzeit):
		self.kochLever += kochzeit
		if self.kochLever >= 0 and self.kochLever<3:
			self.kochString = "shengde"
		elif self.kochLever >=3 and self.kochLever <5:
			self.kochString = "banshengbushou"
		elif self.kochLever >=5 and self.kochLever <8:
			self.kochString = "shoule"
		elif self.kochLever > 8:
			self.kochString = "hule"

	def addZutat(self,zutat):
		self.zutat.append(zutat)

di_gua = susskatoffel()
print(di_gua)

#kaishi kao digua
di_gua.koch(1)
print(di_gua)

di_gua.addZutat("lajiao")

di_gua.koch(1)
print(di_gua)

di_gua.addZutat("ziran")
di_gua.koch(1)
print(di_gua)

di_gua.addZutat("dasuan")
di_gua.koch(1)
print(di_gua)

di_gua.koch(1)
print(di_gua)
di_gua.koch(1)
print(di_gua)
di_gua.koch(1)
print(di_gua)
di_gua.koch(1)
print(di_gua)
di_gua.koch(1)
print(di_gua)
