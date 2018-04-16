
def openfile():
	f = open("hello.txt","r")
	global inhalt
	#content = ""
	while True:
		content = f.read(1024) # read 1024 Byte for one time
		inhalt =inhalt+content
		#print(inhalt)
		if len(content)==0:
			break
	print(inhalt)
	f.close()

def neuDatei():
	f = open("hello_kopie.txt","w")
	global inhalt
	f.write(inhalt)
	f.close

inhalt = ""
openfile()
neuDatei()
'''
def datei_kopie():
	f = open("hello.txt","r")
	w = open("hello_kopie","w")
	while True:
		content = f.read(1024)
		w.write(content)
		if len(content)==0:
			break

	print(content)
	f.close()
	w.close()

datei_kopie()
'''
