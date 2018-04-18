#buguan zenme chuang jian zhi you yige

class Dog(object):
	__instance = None

	def __new__(cls,name):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:  # shang yi ci chuangjian de yingyong
			return cls.__instance
	def __init__(self,name):
		self.name = name
	
a = Dog("wangcai")
print(id(a))
print(a.name)
b = Dog("xiaotianquan")
print(id(b))
print(b.name)
print("==========")
print(a.name)

#print(id(a))
#print(id(b))
