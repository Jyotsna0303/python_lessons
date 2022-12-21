#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 7
print('x is {}'.format(x))
print(type(x))

#built in data types: int, float, str, bool, NoneType. These all are classes

#str
x = 'seven'
y = "seven"
z = '''
seven
'''  #multiline string
a = """ seven """ #same as z
#all are of typestr

#string literals are also objects
x = 'seven night'.capitalize() #Seven night
x = 'seven'.upper()


# For numeric python has int and float.
x = 7/3
print('x is {}'.format(x))
print(type(x)) #class float

x = 7 // 3  # 2, class int floor division

x = 7 %3 # 1, class int

x=.1 +.1+.1 - .3 # 5.551115123125783e-17
#above wont return 0 but return this small number. So we cant use float for money. to solve this python has a module called decimal

from decimal import *
a= Decimal('.10')
b= Decimal('.30')
x = a + a + a - b #0.00 type = decimal.Decimal



#bool class

a = True
b = False
c = 7 > 5 # True


