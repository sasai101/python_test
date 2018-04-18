class ShortInputEx(Exception):
	def __init__(self,lang, atlang):
		self.lang = lang
		self.atlang = atlang

def main():
	print("XXXX")
	try:
		s = input("xxxx: ")
		if len(s)<3:
			raise ShortInputEx(len(s),3)

	except ShortInputEx as result: #result = ShortInputEx(xxx,xxx)
		print("dein eingabe ist %d lang, es muss %d lang sein"%(result.lang, result.atlang))
	else:
		print("Keinen Fehler")
	
main()
