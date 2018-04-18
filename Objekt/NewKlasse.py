class Game(object):
	#Attri von Klasse
	num = 0

	# shili fang fa
	def __init__(self):
		#shi li shu xing
		self.name = "laowng"

	#xiu gai Attri von Klasse
	@classmethod
	def add_num(cls):
		cls.num = 100

	# jin tai fang fa
	@staticmethod
	def print_num():
		print("--------------------")
		print("      CSGo    ")
		print("1. Start game")
		print("2. End game")
		print("--------------------")

game = Game()
#Beide geht.
game.add_num()
#Game.add_num()

print(Game.num)
#diaoyong jin tai fangfa
#1.Game.print_num()
game.print_num()
