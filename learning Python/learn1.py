
'''
# regular expressions

import re
regex = re.compile('x(?P<first>[xy]+)(?P<second>y)')
match = regex.search('xyxxxyxxxyxyxy')
print(match.groupdict())
def all_matches(text, pattern):
	print(pattern)
	regobj = re.compile(pattern)
	for m in regobj.finditer(text):
		print(str(m.start()) + '-' + str(m.end()) + ':' + text[m.start() : m.end()])

#all_matches('xyyxxxxxyyyyxxxxxyy', 'xy*')
#all_matches('xyyxxxxxyyyyxxxxxyy', 'xy+')
#all_matches('xyyxxxxxyyyyxxxxxyy', 'xy?')
#all_matches('xyyxxxxxyyyyxxxxxyy', 'xy{2}')
#all_matches('xyyxxxxxyyyyxxxxxyy', 'xy{2,}')
#all_matches('xyyxxxxxyyyyxxxxxyy', 'xy{3,4}?')
#all_matches('A94B2c4', '[A-Z][0-9]') # finding all when having any letter A-Z following by a number 0-9
#all_matches('A94B2c4 xyz04', '[A-Za-z][0-9]') # finding all when having any letter A-Z and a-z following by a number 0-9
#all_matches('Silk road  does not ', 'S.+k') # letter starting with S and ending with k
#all_matches('This is 1-st example 2',r'\d+') # anything with number 
#all_matches('This is 1-st example 2',r'\D+') # anything but not  number 
#all_matches('This is 1-st example 2',r'\s+') # anything with spaces and similar for S anything but spaces
#all_matches('This is 1-st example 2',r'\w+') # anything with alphanumeric an similar with W for anything but
#all_matches('Relative position in regular expression',r'\br|w+') # littre r at the begining or word
all_matches('Relative position in regular expression',r'\Bg\B')
import re
regex = re.compile('pattern')
#print(regex.search('Searching pattern in text ...').start())
#print(regex.findall('Searching pattern in text pattern...'))
print(re.match('Match', 'Match function test'))
print(re.match('test','Match function test . '))
import re

match = re.search('pattern','Searching pattern in text')
print(match.re.pattern)
print(match.string)
print(match.start())
print(match.end())
#debugging
#opn the debugger and write in command prompt as
# python -m pdb test.py
# break 11 - make abreak point at line number 
# break functionname
#tbreak = break temporary 
#enable 1 = enable break point
# disable = disable break point
# break 4, n >3
#clear 4 = delete the break point
# ignore 2 2 = ignore next two crossing
# commands 2 = u can write a command like print('n =' + str(n))
# jump 11 = jump to particular line 


def IsPrime(n):
	for x in range(2,n // 2+1):
		if not n % x:
				return False
	return True

def Primesto(n):
	for x in range(2,n):
		if IsPrime(x):
			print(x)

Primesto(50)
import pdb
# step = runs next statement
# next = does not run the inside the function
# until = complet the loop 

def fun1(a):
	if a % 2:
		return True
	else:
		return False
def fun2(x):
	if type(x) is int:
		pdb.set_trace()
		print(fun1(x))
	else:
		print('not defined')

fun2(3)
for i in range(5):
	print ('Statement' + str(i+2))
pdb.set_trace()
print('Statement 7 ')

#debugging
import pdb
print('Statement 1')
for i in range(5):
	print ('Statement' + str(i+2))
pdb.set_trace()
print('Statement 7 ')

# Numpy library 
import numpy as np
x=np.linspace(0,6,27)
#print(np.cos(x))
x = np.arange(9).reshape(3,3)
#print(np.exp(x))
#print(x-4)
#print(x**2)
y = np.arange(10,19).reshape(3,3)
#print(x*y)print(x-y)
a = np.array([[1,1],[2,2],[3,3]])
b = np.array([[1,2,3,4,5],[1,2,3,4,5]])
#print(a.dot(b)) print(np.dot(a,b))
# Numpy library 
import numpy as np
v1 = np.array([2,1,3,4])
v2 = np.array([5,4,3,2])
print(np.vstack((v1,v2)))
print(np.hstack((v1,v2)))
a1 = np.array([2,1,4,5])
a2 = np.array([[1,2,3,4,1],[1,2,3,21]])
a3 = np.array([[[1,1,1],[1,1,1]] , [[2,2,2],[2,2,2]], [[3,3,3],[3,3,3]]])
a4 = np.arange(10,100,10) # start and end and diff
a5 = np.arange(15) # from 1 to 15
a6 = np.arange(10,20) # start from 10 till 20 
a6 = np.arange(10.45,15.24,0.2) 
a8 = np.linspace(3,8,9) # 8 steps between 3 and 9 
o1 = np.ones((2,2))
o2 = np.zeros((2,2))
e1 = np.empty((3,4))
e2 = np.eye(3)
r1 = np.random.random((4,5))
c1 = np.arange(15)
b1 = c1>9
c1[b1] = 1 #[0 1 2 3 4 5 6 7 8 9 1 1 1 1 1]
c2 = np.arange(25).reshape(5,5)
c3 = c2.copy() # make not change in c3 if c2 is changed
c3[0,0] = 16
print(c2 is c3)
#Pandas CSV file 
import pandas as pd
df = pd.read_csv("AirPassengers.csv")
print(df['AirPassengers'])
print(df['time'][135])
names = ['Wade', 'James','Kobe','Curry']
total = [55,36,56,54]
data_set= list(zip(names,total))
data_frame = pd.DataFrame(data = data_set, columns = ['Names','Total'])
data_frame.to_csv('Points.csv', index = False, header = True)

#Visualization in Python
import matplotlib.pyplot as plt

fig8 = plt.figure("Pie")
sizes = [50,50,44,36]
labels = ['Wade','James','Kobe','Curry']
explode = (0.1,0,0,0)
colors= ['red', 'purple', "yellow",'blue']
plt.pie(sizes, explode = explode, labels = labels, colors = colors, autopct = '%1.1f%%', shadow = True, startangle = 140)
plt.axis("equal")
plt.show()
#Visualization in Python
import matplotlib.pyplot as plt
fig6 = plt.figure("Scatter")
ax5 = fig6.add_subplot(1,1,1)
ax5.scatter([-1,0,2,3,5],[2,1,3,0.5,4],[1000,200,400,10,4000],['r','g','b','y'])
plt.show()


fig = plt.figure("Histogram")
ax = fig.add_subplot(1,1,1)
ax.hist([12,23,23,35,46,57,65,87,89,76],bins = 7, facecolor = 'g', normed = False)

plt.title("Dictribution")
plt.xlabel("Range")
plt.ylabel("Amount")
plt.show()

fig2 = plt.figure('Box-plot')
ax1 = fig2.add_subplot(1,1,1)
ax1.boxplot([12,23,23,35,46,57,65,87,89,76])
plt.show()

fig3 = plt.figure('Bar')
ax2 = fig3.add_subplot(1,1,1)
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
ax2.set_title('Bars')
ax2.bar([0,1,3,4],[5,10,15,5],[0.51,1,1.3,1],color=['b','r'])
plt.show()

fig4 = plt.figure('Line')
ax3 = fig4.add_subplot(1,1,1)
ax3.set_xlim([-2,10])
ax3.set_ylim([0,6])
ax3.set_xlabel('X')
ax3.set_ylabel('Y')
ax3.set_title("Lines")
ax3.plot([-1,2,4,6,7],[5,4,3,2,1],'r')
plt.show()
data = {'Player':['Wade','James','Kobe','Curry'],
		'First':[10,10,8,12],
		'Second':[12,7,6,23],
		'Third':[15,12,8,8],
		'Fourth':[18,20,15,9]}

fig5 = plt.figure("Stacked Bar")
ax4 = fig5.add_subplot(1,1,1)
bar_width = 0.5
bars = [i+1 for i in range(len(data['First']))]
ticks = [i + (bar_width/2) for i in bars]
ax4.bar(bars,data['First'],width = bar_width,label= 'First Quarter',color = '#AA5439')
ax4.bar(bars,data['Second'],width = bar_width,bottom=data['First'], label= 'Second Quarter',color = '#FFD600') 
ax4.bar(bars,data['Third'],width = bar_width,bottom=[i+j for i,j in zip(data["First"],data["Second"])], label= 'Third Quarter',color = '#FF9200') 
ax4.bar(bars,data['Fourth'],width = bar_width,bottom=[i+j+k for i,j,k in zip(data['First'],data['Second'],data['Third'])], label= 'Fourth Quarter',color = 'r')
plt.xticks(ticks,data['Player'])
ax4.set_xlabel("total")
ax4.set_ylabel("Player")
plt.legend(loc = 'upper right')
plt.xlim([min(ticks)- bar_width, max(ticks)+bar_width])
plt.show()
#Visualization in Python
#matplotlid: basic library for data visualization in Python
#some other: vispy, bokeh,seaborn,pygal,folium pandas
#constructor  # destructure 
class Student(object):
	"""Student"""
	number_of_students = 0

	def __init__(self,name,index):
		self.name = name
		self.index = index
		Student.number_of_students +=1

	def __del__(self):
		Student.number_of_students -=1

s1= Student("Ali", 12345)
s2= Student("mohammad", 123)

print(Student.number_of_students, s1.number_of_students, s2.number_of_students)
del s1
print(Student.number_of_students)

import math
class Complex:
	'This class simulates complex numbers'
	def __init__(self,real = 0,imag = 0):
		if(type(real) not in (int,float)) or (type(imag) not in (int,float)):
			raise Exception("Args are not numbers! ")
		self.SetReal(real) # underscore means varaible are private
		self.SetImag(imag) # another way to initialize the values
	def GetReal(self):
		return self.__real

	def GetImag(self):
		return self.__imag

	def GetModulus(self):
		return math.sqrt(self.GetReal()*self.GetReal() + self.GetImag()*self.GetImag())

	def GetPhi(self):
		return math.atan2(self.GetImag(),self.GetReal())

	def SetReal(self,val):
		if type(val) not in (int,float):
			raise Exception("real part must be a number")
		self.__real = val
	def SetImag(self,val):
		if type(val) not in (int,float):
			raise Exception("imag part must be a number")
		self.__imag = val

	def __str__(self):
		return str(self.GetReal()) + '+' + str(self.GetImag()) + 'i';

	def __add__(self,other):
		return Complex(self.GetReal() + other.GetReal(),self.GetImag()+ other.GetImag())

	def __mul__(self,other):
		if type(other) in (int,float):
			return Complex(self.GetReal() * other, self.GetImag()*other)
		else:
			return Complex(self.GetReal()*other.GetReal()-self.GetImag()*other.GetImag(),
				self.GetImag()*other.GetImag()+self.GetReal()*other.GetReal())

	def __truediv__(self,other):
		if type(other) in (int, float):
			return Complex(self.GetReal()/float(other), self.GetImag()/float(other))
		else:
			a , b, c, d = self.GetReal(),self.GetImag(),other.GetReal(),other.GetImag()
			nominator = c*c + d*d
			return complex((a*c + b*d)/nominator, (b*c-a*c)/nominator)

	real = property(GetReal,SetReal)
	imag = property(GetImag,SetImag)		


# class inheritance
class Vehicle:
	def __init__(self,VIN,weight,manufac):
		self.vin_number = VIN
		self.weight = weight
		self.manufac = manufac

	def GetWeight(self):
		return self.weight

	def GetManufac(self):
		return self.manufac

	def VehicleType(self):
		pass

class Car(Vehicle):
	def __init__(self, VIN, weight,manufac,seats):
		self.vin_number= VIN
		self.weight =	weight
		self.seats = seats	
		self.manufac = manufac

	def NumberofSeats(self):
		return self.seats

	def VehicleType(self):
		return 'CAR'

class Truck(Vehicle):
	def __init__(self,VIN,weight,manufac,capacity):
		self.vin_number= VIN
		self.weight = weight
		self.capactiy = capacity	
		self.manufac = manufac

	def TransportCapacity(self):
		return self.capactiy

	def VehicleType(self):
		return 'TRUCK'

a = Car('ABC1', 1000, 'BMW',4)
b = Truck('BCD2', 1000, 'MAN', 10000)
c = Car('DEF3', '1200', 'ford',4)
d = Truck('EFG4', 11000,'mercedes', 15000)

print(a.GetWeight(),b.GetManufac(),c.NumberofSeats(),d.TransportCapacity())
import math
class Complex:
	'This class simulates complex numbers'
	def __init__(self,real = 0,imag = 0):
		if(type(real) not in (int,float)) or (type(imag) not in (int,float)):
			raise Exception("Args are not numbers! ")
		self.SetReal(real) # underscore means varaible are private
		self.SetImag(imag) # another way to initialize the values
	def GetReal(self):
		return self.__real

	def GetImag(self):
		return self.__imag

	def GetModulus(self):
		return math.sqrt(self.GetReal()*self.GetReal() + self.GetImag()*self.GetImag())

	def GetPhi(self):
		return math.atan2(self.GetImag(),self.GetReal())

	def SetReal(self,val):
		if type(val) not in (int,float):
			raise Exception("real part must be a number")
		self.__real = val
	def SetImag(self,val):
		if type(val) not in (int,float):
			raise Exception("imag part must be a number")
		self.__imag = val

	def __str__(self):
		return str(self.GetReal()) + '+' + str(self.GetImag()) + 'i';

	def __add__(self,other):
		return Complex(self.GetReal() + other.GetReal(),self.GetImag()+ other.GetImag())

	def __mul__(self,other):
		if type(other) in (int,float):
			return Complex(self.GetReal() * other, self.GetImag()*other)
		else:
			return Complex(self.GetReal()*other.GetReal()-self.GetImag()*other.GetImag(),
				self.GetImag()*other.GetImag()+self.GetReal()*other.GetReal())

	def __truediv__(self,other):
		if type(other) in (int, float):
			return Complex(self.GetReal()/float(other), self.GetImag()/float(other))
		else:
			a , b, c, d = self.GetReal(),self.GetImag(),other.GetReal(),other.GetImag()
			nominator = c*c + d*d
			return complex((a*c + b*d)/nominator, (b*c-a*c)/nominator)

	real = property(GetReal,SetReal)
	imag = property(GetImag,SetImag)

c2 = Complex(-3,4)
c1 = Complex(5,0.3)
print(c1 + c2 )
print(c1 * c2 )
print (c1/c2)
print(c1/2)


# OOP
class Complex:
	'This class simulates complex numbers'
	def __init__(self,real = 0,imag = 0):
		if(type(real) not in (int,float)) or (type(imag) not in (int,float)):
			raise Exception("Args are not numbers! ")
		self.__real = real # underscore means varaible are private
		self.__imag = imag
	def GetReal(self):
		return self.__real
	def GetImag(self):
		return self.__imag
	def SetReal(self,val):
		if type(val) not in (int,float):
			raise Exception("real part must be a number")
		self.__real = val
	def SetImag(self,val):
		if type(val) not in (int,float):
			raise Exception("imag part must be a number")
		self.__imag = val


c= Complex()
try:
	c.SetReal((1,2,3))
except Exception as e:
	print(e)

class Complex:
	'This class simulates complex numbers'
	def __init__(self,real = 0,imag = 0):
		if(type(real) not in (int,float)) or (type(imag) not in (int,float)):
			raise Exception("Args are not numbers! ")
		self.real = real
		self.imag = imag


try:
	c= Complex(2,4)
	print(c.real,c.imag)
except Exception as e:
	print(e)

# modules and packages
#import copy
import copy
my_dict = {'Key': 'Value', ('K','E','Y'):5}
my_dict1 = copy.deepcopy(my_dict)
my_dict[1] = 1
#print(my_dict)
#print(my_dict1)

import math as m
import cmath as cm
import random as ran
import sys
#print(m.cos(m.pi))
#print(m.exp(1))
#print(dir(cm))
#print(cm.sqrt(4))
#print(cm.polar(complex(0,1)))
#print(ran.sample([1,2,3,4,5,6] , 3))
#print(ran.randint(5,100))
#print(sys.getrecursionlimit())
#print(sys.version)



# modules and packages
#import Prime as pr # use Prime as shorter name of pr
#from Prime import PrimesTo # import just a function 
#PrimesTo(100) # 
#import Prime
#print(dir(Prime))

import main.sub2.Prime as sub2
sub2.PrimesTo(100)
# set functions
my_set=set(['one','two','three','one'])
my_set1 =set(['two', 'three','four'])
print(set.union(my_set,my_set1))
print(set.intersection(my_set,my_set1))
print(set.difference(my_set,my_set1))
#set
my_set=set(['one','two','three','one'])
print(my_set) #{'one', 'two', 'three'} duplicate removed
my_set1 =set(['two', 'three','four'])
print(my_set1 | my_set) # {'three', 'one', 'four', 'two'} union of set 
print(my_set1 ^ my_set) # {'one', 'four'} intersection 
a = my_set1 - my_set
print(a) # {'four'} difference
my_set.add('five')
print(my_set) # {'one', 'five', 'two', 'three'} add a element
# shallow copies with dict
my_dict = {'Item' : 'Shirt', 'Size':"Medium", "Price": 50}
my_dict1 = my_dict
print(my_dict)
my_dict["Size"] = "Small"
print(my_dict1)
# data structures Dictionary
my_dict = {'Key':'Value' , ('K', "E", "Y"):5}
my_dict1 = {x:x+1 for x in range(10)}
print(my_dict["Key"]) # key is associated with value so we get Value
print(my_dict1) #{0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 10}
print(my_dict.keys()) #dict_keys([('K', 'E', 'Y'), 'Key'])
print(my_dict.values()) #dict_values([5, 'Value'])
my_dict[23] = 2
print(my_dict) #{'Key': 'Value', ('K', 'E', 'Y'): 5, 23: 2}
del my_dict[23]
print(my_dict) #{'Key': 'Value', ('K', 'E', 'Y'): 5}
my_dict.clear() #{}
print(my_dict)
# list functions
import functools
print(list(map(lambda x: x**2 + 3 **x +1 , [1,2,3,4]))) #[5, 14, 37, 98] applied every element in list to equation 
print(list(filter(lambda x: x < 4, [1,2,3,4,5,6,7]))) # return every element that i less than 4
print(functools.reduce(lambda x,y: x*y, [1,2,3,4])) # 24 ??

# data Structures
# list 
list1 = [1,'abc', (2,3)]
print(list1[2]) # (2,3)
print(list1[2][0]) # 2
print(list1 + ['4']) #[1, 'abc', (2, 3), '4']
print(list1 * 2) #[1, 'abc', (2, 3), 1, 'abc', (2, 3)]
print (2 in list1) # false 
print(list1 == [1,'abc',(2,3)]) # true
print(list1[:2]) # [1, 'abc']
list1.append(6)
list1[len(list1):] = [7]
print(list1) #[1, 'abc', (2, 3), 6, 7]
# some useful function with tuples
tup = (534 ,2343, 2344)
print(max(tup))
print(len(tup))
print(min(tup))

tup = (1,'abc',2,'cde')
tup1 = 3, 'efg', True
tup2 = 'A' # tup2 = ('A',)
print (tup) # (1,'abc',2,'cde')
print(tup[0]) # 1 
print(tup[0:2]) #(1, 'abc')
try:
	tup[3] = 5
except Exception as e:
	print(e) #'tuple' object does not support item assignment

tup = tup[0:3] + (34,) # add another element in tup
print(tup2 * 4) # AAAA
print(5 in tup) # False
for x in ('a', 'b','c'):
	print(x) # a b c 

def multiple_result():
	return (1,2,'a') 
print (multiple_result()) # (1,2,'a')
print((1,2,3) == (1,2)) # fasle
#open(filename,access,buffering)
file = open("C:\\Users\\la5w7\\Desktop\\misc.txt", "w+")
file.write("Hello file. I am string!")
file.seek(0)
file.write("this")
file.seek(0)
print(file.read())
file.close()
file = open("C:\\Users\\la5w7\\Desktop\\misc.txt", "r")
print("File Name: "+ file.name) # File Name: C:\Users\la5w7\Desktop\misc.txt
print("is closed "+str(file.closed)) # is closed False
print("Mode "+ file.mode) # Mode r
#for line in file:
	#print(line) # print all line in misc.txt
file.close()
file = open("C:\\Users\\la5w7\\Desktop\\misc.txt", "r")
print(file.read(4)) # VIN:
file.seek(5) # move cursor to after reading
print(file.tell()) #5

age = input("How are you:")
print(age)
def testcase(a,b):
	assert a<b,"a is greater than b"
try:
	testcase(1,2)
except AssertionError as e:
	print(e)

a = 12
def RaiseException(a):
	if type(a) != type('a'):
		raise ValueError("This is not string")

try:
	RaiseException(a)
except ValueError as e:
	print(e)

try:
	n = int(input("enter an integer: "))
except ValueError:
	print('that is not integer')

f= lambda a:lambda b: lambda c:a*b*c
print(f(2)(3)(4))
f = lambda x,y:x+y
print(f(2,3))
def sum(n):
	if n == 1:
		return 1
	else:
		return n + sum(n-1)

def tail_sum(n,accu = 0):
	if n ==0:
		return accu
	else:
		return tail_sum(n-1,accu +n)

print(sum(10))
print(tail_sum(10))
def fact(n):
	if n ==1:
		return 1
	else:
		return n*fact(n-1)
print(fact(5))
def f(a):
	def g(b):
		def h(c):
			return a*b*c
		return h
	return g

print(f(5)(2)(3))
def outer(a):
	def nested(b):
		return b*a;
	a = nested(a)
	return a
print(outer(4))
def scope(a):
	a = a+1
	print(a)
	return a
scope(5)
def out(a):

		def nested(b):
			return b * a 
		a = nested(a)
		return a

def add(a,b=3,c=4):
	return a+b+c

def parameter(a):
	print(a)

r = add(1,2)
print(r)
print("This is a parameter")
print(out(20))

def scope(a):
	a = 1+a
	print(a)
	return a
scope(5)

def def_para(a  = 2, b = 4 , c = 5):
	return a + b +c 
result = def_para(111,5454,24234)
print(result)

def add(a,b):
	c = a+b
	return c 
result = add(2,5)
print(result)
result = add("one", "two")
print(result)
def parameter(a):
	print(a)
parameter("this is a parameter")

def returning():
	return "I am a result!",2
print(returning())
def function():
	print("This is our first function")
function()
while True:
	print("Infiite")
	break

for i in range(1,11):
	if i == 5:
		continue
	print(i)


for i in range(1,11):
		print('{:<3}|'.format(i),end="")

		for j in range(1,11):
			print("{:>4}".format(i*j),end="")

		if i == 1:
			print('\n {:#^44}'.format(""),end="")

		print("")
for i in range(3):
	for j in range(2):
		print(j)
#range(start,stop,step)
string = "String taversal!"
for char in string:
	print(char)
for i in range(len(string)):
		print(string[i])
for i in range(1,10,2):
	print(i)
passerby_speech = 'Hi'
if passerby_speech == 'hello':
	print("Hi how are you ?")
elif passerby_speech == "Hi":
	print("Hello")
else:
	print("Hey")
passerby_speech1 = "Hello"
me = "Hi" if passerby_speech1 == "HEllo" or passerby_speech1 == "HI" else "Hey"
print(me)
a= 3,
a =7 if 3**2 > 9 else 14
print(a)

# if condition_statement:
	#code
	#print
#if condition1
	#code
#elif condtion2
	#code
#else
	#code

#< > <= >= 
print (5<6)
print (2>=3)
print ('abc' == 'abc')
#not and or
a = True
b = False	
print ( not a )
print (a and b)

print('I\'m a string in "Python"')
print(r'C:\number\nan')
print("""\
	Hello:
		User defined look 
		Pything output
		""")
print("today i had {0} cup of {1}". format(3,"Coffee")) # I today i had 3 cup of coffee
print('price : ({x} , {y} ,{z})'.format( x = 2,y = 45, z = 324))
print("The {vehicle} had {0} crashes in {months} months".format(5,vehicle = 'car',months = '1'))
print("{:<20}".format("text")) 
print("{:>20}".format("text"))
print("{:b}".format(21))
print("{:x}".format(21))
print("{:o}".format(21))

string1 = 'I was a string paython'
string2 = "I will be a string in python"
string3 = 2* ('Com' + 'contenation')
print(string3)
print (string1 + string2)
word = 'Ford'
word = 'L' + word[1:]
print(word)


print(len('My length is 15'))
print(len (string1))
print(string1[-2]) # u will get printed o
print(string1[5:11])
print(string1[:11])
print(string1[11:])
# order of arthimatic operation() ** * / * + - 
# print(32 >>2 ) 32 converted in bit and then 2 time shifted
#print (256 & 255) you get end result as 0 
# print (256 | 255) you get OR function
# print (60^13) it is xor function 
inside a bunch of comments 
can be write anything here
print(2.5+5)
print(2**5) # power of value
print(2/5)
print(23//5) # floating point number
print(23.5/5)
print(45.0%4)
a = 2+5
b= 3.3 * 3
c = 10/5 

'''