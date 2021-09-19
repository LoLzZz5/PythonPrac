import math
from math import *

def f11(x,y):
	f = sqrt((x**6 + abs(y)-46)/(abs(y)-47*x**7)) + sqrt((36*y**2 -6*x**3)/(math.sin(y)-x))+(y**6)/79 -y
	return f

def f12(x):
	if x < 117:
		f = math.exp(x)+x**7 +math.cos(x)
		return f
	elif x>=117 and x<166:
		f = math.cos(72*x**3)+95*x**8
		return f
	elif x>=166:
		f = 38*x**7 - 72*x**6
		return f

def f13(x,y):
	count=0
	for i in range(1,x+1):
		count+=(i+i**3)/73
		for j in range(1,y+1):
			count-=(math.log10(j)+i**5)/40
	return count

def f14(x):
	if x == 0:
		return 6
	else:
		return abs(f14(x-1))-(1/19)*f14(x-1)**2

def f21(x):
	if x[3]==2015:
		return 12
	elif x[3]==1970:
		if x[2]==1975:
			return 11
		elif x[2]==2012:
			return 10
		elif x[2]==2001:
			return 9
	elif x[3]==2006:
		if x[1]=='mql5':
			if x[0]==1983:
				return 8
			elif x[0]==1994:
				return 7
			elif x[0]==1961:
				return 6
		elif x[1]=='idris':
			if x[0]==1961:
				return 3
			elif x[0]==1994:
				return 4
			elif x[0]==1983:
				return 5
		elif x[1]=='tea':
			if x[2]==1975:
				return 2
			elif x[2]==2012:
				return 1
			elif x[2]==2001:
				return 0

def f22(x):
	d = x & 0x80000000
	c = x & 0x7fe00000
	b = x & 0x1FFF00
	a = x & 0xFF
	
	d = d >> 23
	c = c << 1
	b = b << 1
	a = a << 0

	x = d+c+b+a
	return x

class C32:
	def __init__(self):
		self.condition = 'A'
	def cue(self):
		if self.condition == 'A':
			self.condition ='B'
			return 0
		elif self.condition == 'B':
			self.condition ='E'
			return 2
		elif self.condition == 'D':
			self.condition = 'E'
			return 4
		else:
			RuntimeError
	def trash(self):
		if self.condition =='B':
			self.condition = 'C'
			return 1
		elif self.condition =='D':
			self.condition ='F'
			return 6
		elif self.condition =='E':
			self.condition = 'E'
			return 8
		else:
			RuntimeError
	def amass(self):
		if self.condition =='C':
			self.condition ='D'
			return 3
		elif self.condition =='D':
			self.condition ='D'
			return 5
		elif self.condition =='E':
			self.condition ='F'
			return 7
		else:
			RuntimeError
			
# print(f11(-7,70))
# print(f11(-68,-61))
# print(f12(183))
# print(f12(216))
# print(f13(53,10))
# print(f13(38,37))
# print("%.2e" % f14(6))
# print("%.2e" % f14(15))
# print(f21([1994,'mql5',2012,1970]))
# print(f21([1983,'mql5',1975,2015]))
# print(f22(0x9b7db461))
# print(f22(0x2d6c9a59))