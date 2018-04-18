# Erste Exception

try:
	open("XXX.txt")
	print(mun)
	print("------1------")
except (NameError,FileNotFoundError): # duo yi chang yong yuan zu
	print("Reaktion, wenn ein Exception gefunden wird")
	print("keinen passenden Datei")

print("------2------")
