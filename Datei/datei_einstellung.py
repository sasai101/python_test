import os

def datein_rename():
	os.rename("hello.txt","test.txt")

def datein_remove():
	os.remove("test.txt")

def datein_erstellen():
	os.mkdir("also")

#datein_rename()
#datein_remove()
datein_erstellen()
