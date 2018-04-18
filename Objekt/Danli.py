#buguan zenme chuang jian zhi you yige

class Dog(object):
	__instance = None

	def __new__(cls):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:  # shang yi ci chuangjian de yingyong
			return cls.__instance
	
a = Dog()
b = Dog()
print(id(a))
print(id(b))
