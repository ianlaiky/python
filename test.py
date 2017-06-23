# print("test")
# print("test")
# print("test")

# a = 100
# b = 100.7

# c=a+b
# print(c)

# a = 3.4567
# b = 4
# c = a+b
# print("{}+{}={}".format(a,b,c))
# print ("{1}+{0}={2}".format(a,b,c))
# print("{:0.2f}+{:0.2f}={:0.2f}".format(a,b,c))

# a=4
# b=5
# c=6
# d=a+b+c
# print("{}+{}+{}={}".format(b,c,a,d))

# a ='Hello '
# b = "World!"
# c = a+b
# print(c)
# e = c.upper()
# print(e)
# print(dir(e))


# country = "France"
# capital = "paris"
# print("The capital of {} is {}".format(country.upper(),capital))

# a = "Today is a sunny day"
# b = a.split()
# print(b)
# print(b[3])
# c = ",".join(b)
# print(c)

# a = "hello@Tertiaryinfotech.com"
# b = " at ".join(a.split("@"))
# print(b)


# c = "atgcgcatgcac"
# b=c.count("at")
# print(b)

# a = 10
# b = a
# a=a+1
# print(a)
# print(b)

# letters = ["A","C","C","A","T","T","G","A","C","A"]

# print(letters.count("A"))
# print(letters.index("T"))

# letters2 = letters.copy()
# letters2.remove("G")
# print(letters2)
# letters2.insert(2,"A")
# print(letters2)
# letters2.reverse()
# print(letters2)

# a = (1,2,3,4,5)
# print()

# a=5
# b=3

# if(a>b):
#  	print("A is smaller than b")
#  	print("fsdfds")
# else:
#  	print("B is smaller than a")

# grade = "B"

# if(grade=="A"):
# 	print("Excellent!")
# elif(grade=="B"):
# 	print("Well done!")
# elif(grade=="C"):
# 	print("Work harder")
# else:
# 	print("I dont know your grade")

# a =1
# while(a<10):

# 	print(a)
# 	a=a+1
# b=1
# a=0
# while(b<100):
# 	a,b=b,a+b
# 	print(b)
# for x in range(1,101,2):
# 	print("X = ",x)

# s = "This is a string"
# for c in s:
# 	print(c)

# a=[1,2,3,4,5,6]
# b=['a','b','c','d','e','f']

# c = zip(a,b)

# for i in c:
# 	print(str(i[0])+i[1])

# name=["Ally","Belinda","Jane"]
# height=[170,159,161]
# weight=[60,55,45]

# user = zip(name,height,weight)
# for x in user:
# 	print(x)
# primes=[]
# for num in range(1,101):
# 	for i in range(2,num):
# 		if (num%i==0):
# 			break
# 	else:
# 			primes.append(num)
# print(primes)

# def f(x):
# 	return x*x


# print(f(4))


# def calculateFare(bookFee,startingPrice,distance,costPerKm):
# 	return bookFee+startingPrice+distance*costPerKm


# print("Taxi fare is: ${:0.2f}".format(calculateFare(10.5842,124,123,12)))

# def f(x):
# 	return (x*x,2+x)
# a=f(10)
# print(a[0],a[1])

# def purchase(order):

# 	if(order>200):
# 		disc=25
# 	else:
# 		disc=0
# 	tax = 0.07*(order-disc)
# 	return disc,tax
# a = purchase(387.5)
# print("The discount is: {:0.2f} And the tax is: {:0.2f}".format(a[0],a[1]))

# a=[3,4,7,3,1,10]
# def getMinValue(x):
# 	temp = x[0]
# 	for i in x:
# 		if(i<temp):
# 			temp=i
# 	return temp
# print(getMinValue(a))


# f = lambda x: x*x
# print(f(10))

# cal = lambda x,y: 10*x+y

# print(cal(3,4))

# a = [3,4,5,6,7]
# f = lambda x:x**2

# print(list(map(f,a)))

# f = lambda x,y:10*x+y
# x=[0,1,2,3]
# y=[2,4,6,8]

# print(list(map(f,x,y)))


# from openpyxl import Workbook
# wb = Workbook()

# # grab the active worksheet
# ws = wb.active

# # Data can be assigned directly to cells
# ws['A1'] = 42

# # Rows can also be appended
# ws.append([1, 2, 3])

# # Python types will automatically be converted
# import datetime
# ws['A2'] = datetime.datetime.now()

# # Save the file
# wb.save("sample.xlsx")

# import module1

# print(module1.add(1,2))
# a=[n**2 for n in range(10) if n%2==0]
# print(a)
# b = "Today is a rainny day"


# a=[n[:1] for n in b.split() if("a" in n and len(n)>3)]
# print(a)


# def f(i):
# 	return i*i


# a = [f(i) for i in range(20000) if i%3 and i%5]
# print(a)




# a = (n*n for n in range(1000000000000000000000000))
# for i in a:
# 	print(i)

# namelist = ['Ally','Jane',"Belinda"]
# gen = (n.upper() for n in namelist)
# for a in gen:
# 	print(a)

# def even_number(n):
# 	for i in range(n):
# 		if i%2==0:
# 			yield i

# a = even_number(10000000000000000)
# for x in a:
# 	print(x)

# def fibo():
# 	a,b=0,1
# 	while True:
# 		yield a
# 		a,b=b,a+b
# a = fibo()

# count =0
# for x in a:
# 	print(x)
# 	count = count +1
# 	if(count==5):
# 		break

# class Person():
# 	def __init__(self,name,age,ID):
# 		self.n = name
# 		self.a = age
# 		self.I=ID
# 	def is_old(self):
# 		return self.a
# 	def changeName(self,newName):
# 		self.n = newName
# 		return self.n

# p1=Person("Tim",25,11111)
# print(p1.is_old())
# p1.changeName("james")
# p1.n="poi"
# print(p1.n)

# class Rectangle():
# 	def __init__(self,length,width):
# 		self.length = length
# 		self.width = width
# 	def caculateArea(self):
# 		return self.length*self.width



# r = Rectangle(10,5)

# print(r.caculateArea())

# class Employee():
# 	count=0
# 	def __init__(self,name,salary):

# 		self.name=name
# 		self.salary=salary
# 		Employee.count+=1

# 	def display(self):
# 		return self.name+","+str(self.salary)
# e1 = Employee("Tim",5000)
# print(e1.display())

# e2 = Employee("james",5000)
# print(e2.display())

# print(Employee.count)



# class Person():
# 	def __init__(self,name,gender):
# 		self.name = name
# 		self.gender = gender
# 	def get_details(self):
# 		return self.name
# 	def get_more(self):
# 		return "test"
# class Student(Person):
# 	def __init__(self,name,gender,branch,year):
# 		super().__init__(name,gender)
# 		self.branch=branch
# 		self.year=year
# 	def get_details(self):
# 		return "{} studies {} and is in {} year.".format(self.name,self.branch,self.year)

# p1 = Student("Keb","M","computer",1997)
# print(p1.name)
# print(p1.get_details())
# print(p1.get_more())



# class Rectangle():
# 	def __init__(self,length,width):
# 		self.length = length
# 		self.width = width
# 	def caculateArea(self):
# 		return self.length*self.width


# class Square(Rectangle):
# 	def __init__(self,length):
# 		super().__init__(length,length)

# sq = Square(10)
# print(sq.caculateArea())


class Employee():
	count=0
	def __init__(self,name,salary):

		self.name=name
		self.salary=salary
		Employee.count+=1

	def display(self):
		return self.name+","+str(self.salary)

class FullTimeStaff(Employee):
	def __init__(self,name,salary,leave):
		super().__init__(name,salary)
		self.leave=leave
	def display(self):
		return "{} , {} , {}".format(self.name,self.salary,self.leave)

		self.leave=leave
class PartTimeStaff(Employee):

	def __init__(self,name,hourlyRate):
		super().__init__(name,salary=0)
		self.hourlyRate=hourlyRate
	def display(self):
		return "{},{}".format(self.name,self.hourlyRate)

staff1 = FullTimeStaff("james",1520,5)
staff2 = PartTimeStaff("tim",12)


# print(staff1.display())
# print(staff2.display())

#
# import sqlite3
#
# db = sqlite3.connect('test.db')
# db.commit()
