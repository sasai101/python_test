# Menue anzeigen
def main():
	print("*"*20)
	print("***Verwaltung des Namecard***")
	print("1. Eine neue Namecard erstellen")
	print("2. Eine Namecard loeschen")
	print("3. Eine Namecard veraendern")
	print("4. Eine Namecard Suchen")
	print("5. Alle Namecard zeigen")
	print("7. Speicher")
	print("6. Programm ausschlaten")
	print("*"*20)
	option_Auswaehlen()

def option_Auswaehlen():
	while True:
		wahl = input("Bitte geben Sie eine Option: ")
		zahl = eingabe_beurteilen(wahl)
		if zahl==1:
			name_Eingabe()
		elif zahl==2:
			namecard_loeschen()
		elif zahl==3:
			namen_verandern()
		elif zahl==4:
			name_suchen()
		elif zahl==5:
			print_Namecard()
		elif zahl==7:
			save_2_file()
		elif zahl==6:
			print("BYE BYE :D !!")
			break
		else:
			print("Bitte geben Sie Zahl 1~7")

def name_Eingabe():
	info = {}
	name = input("Bitte Name eingeben: ")
	num = input("Bitte Nummer eingeben: ")
	addr = input("Bitte Adresse eingeben: ")
	info["name"] = name
	info["num"] = num
	info["addr"] = addr
	#global namecard
	namecard.append(info)

def namecard_loeschen():
	such_name = input("Bitte geben Sie einen loeschenden Name ein: ")
	for temp in namecard:
		if temp['name']==such_name:
			del temp['name']
			del temp['num'] 
			del temp['addr']
			namecard.remove({})
			print("Name schon veraendert!!!")
			break
	else:
		print("keine gefunden")

def namen_verandern():
	such_name = input("Bitte geben Sie einen verandernde Name ein: ")
	for temp in namecard:
		if temp['name']==such_name:
			newName = input("Bitte geben Sie eine neuen Name ein: ")
			temp['name'] = newName
			print("Name schon veraendert!!!")
			print("Name\tNummer\tAddresse")
			print("%s\t%s\t%s"%(temp['name'], temp['num'], temp['addr']))
			break
	else:
		print("keine gefunden")

def name_suchen():
	such_name = input("Bitte geben Sie einen suchenden Name ein: ")
	for temp in namecard:
		if temp['name']==such_name:
			print("Name\tNummer\tAddresse")
			print("%s\t%s\t%s"%(temp['name'], temp['num'], temp['addr']))
			break
	else:
		print("keine gefunden")

def print_Namecard():
	global namecard
	try:
		f = open("backup.data","r")
		namecard = eval(f.read())
		print(namecard)
		print("Name\tNummer\tAddresse")
		for temp in namecard:
			print("%s\t%s\t%s"%(temp['name'], temp['num'], temp['addr']))
	except Exception:
		pass
	finally:
		f.close()

def save_2_file():
	"""einspeichern"""
	f = open("backup.data","w")

	f.write(str(namecard))

	f.close

def eingabe_beurteilen(zahl):
	try:
		int(zahl)
		return int(zahl)
	except ValueError:
		print("Bitte geben Sie eine Zahl ein!!")
		option_Auswaehlen()

if __name__ == "__main__":
	namecard = []
	main()
