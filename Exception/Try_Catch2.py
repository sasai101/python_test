# Erste Exception

try:
	11/0
	open("XXX.txt")
	print(mun)
	print("------1------")
except (NameError,FileNotFoundError): # duo yi chang yong yuan zu
	print("Reaktion, wenn ein Exception gefunden wird")
	print("keinen passenden Datei")
except Exception as ret: 
	print("Alle Errors kann mit Exception gefunden werden")
	print(ret) # Error Typ auszudrucken
else:
	print("keine Error")
finally:
	print("es kommt immer vor, obwohl es da Fehler gibt oder nicht!!")

print("------2------")
