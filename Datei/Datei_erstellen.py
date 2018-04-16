
f = open("haha.txt","w")
f.write("heihei")
f.close

f = open("haha.txt", "r")

print(f.read(1))
print(f.read(1))
print(f.read(1))
print(f.read(1))
print(f.read(1))
print(f.read(1))
print(f.read(1))
print(f.read(1))
print(f.read(1))
print(f.read(1))

o = open("haha.txt","r")
content = o.read()

print(content)
f.close()
o.close()
