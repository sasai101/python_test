class Tools(object):
	#Attriebutte
	num = 0
	#Funktion
	def __init__(self, new_name):
		self.name = new_name
		Tools.num += 1

tool1 = Tools("Schaufel")
tool2 = Tools("Eimer")
tool3 = Tools("Werkbox")

print(Tools.num)
