
#class Counter:
#	def reset(self):
#		self.count = 0
#	def increment(self):
#		self.count += 1
#	def get(self):
#		return self.count

#a = Counter()
#a.reset()

#for i in range(5):
#	a.increment()

#print("카운터 a의 값은",a.get())

#class Counter:
#	def __init__(self):
#		self.count = 0
#	def reset(self):
#		self.count = 0
#	def increment(self):
#		self.count += 1
#	def get(self):
#		return self.count

#class Television:
#	def __init__(self,channel,volume,on):
#		self.channel = channel
#		self.volume = volume
#		self.on = on

#	def show(self):
#		print(self.channel, self.volume, self.on)
#	def setChannel(self, channel):
#		self.channel = channel
#	def getChannel(self):
#		return self.channel

#t = Television(9,10,True)
#t.show()
#t.setChannel(11)
#t.show()

#class Student:
#	def __init__(self,name = None, age = 0):
#		self.__name = name
#		self.__age = age
#	def getAge(self):
#		return self.__age
#	def getName(self):
#		return self.__name
#	def setAge(self,age):
#		self.__age =age
#	def setName(self,name):
#		self.__name = name

#obj = Student("Hong",20)
#print(obj.getName())
#print(obj.getAge())

#obj.setName("Bang")
#obj.setAge(25)
#print(obj.getName())
#print(obj.getAge())

#class Vector2D :
#	def __init__(self, x, y):
#		self.x = x
#		self.y = y

#	def __add__(self, other):
#		return Vector2D(self.x + other.x, self.y + other.y)

#	def __sub__(self, other):
#		return Vector2D(self.x - other.x, self.y - other.y)

#	def __eq__(self, other):
#		return self.x == other.x and self.y == other.y

#	def __str__(self):
#		return '(%g, %g)' % (self.x, self.y)

#u = Vector2D(0,1)
#v = Vector2D(1,0)
#w = Vector2D(1,1)
#a = u + v

#if a == w:
#	print("같음")

#print(a)

class Vehicle:
	def __init__(self, make, model, color, price):
		self.make = make # 메이커
		self.model = model # 모델
		self.color = color # 자동차의 색상
		self.price = price # 자동차의 가격
	def setMake(self, make): # 설정자 메소드
		self.make = make
	def getMake(self): # 접근자 메소드
		return self.make
	def getDesc(self):
		return "차량 = ("+str(self.make)+","+str(self.model)+","+str(self.color)+","+str(self.price)+")"

class Truck(Vehicle):
	def __init__(self,make,model,color,price,payload):
		super().__init__(make,model,color,price)
		self.payload = payload
	def setPayload(self,payload):
		self.payload = payload
	def getPayload(self):
		return self.payload

myTruck = Truck("Tisla","Model S","white",10000,2000)
myTruck.setMake("BMW")
myTruck.setPayload(5000)
print(myTruck.getDesc()) 