def open_datein():
	f = open("hello.txt","r")
	print(f.read(8))
	print(f.tell())
	print(f.seek(0,2))
	print(f.read(1))
open_datein()
