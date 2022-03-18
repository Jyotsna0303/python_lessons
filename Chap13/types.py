#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = '47'
y = int(x) #converting string to int

z=divmod(47, 3) #return a tuple (15,2) returns quotiend and remainder

print(f'x is {type(x)}')
print(f'x is {x}')
print(f'y is {type(y)}')
print(f'y is {y}')

#string
#repr(s)-- method to represent the string in a represrentable manner. there is a speical methods __repr__(self)
#in a class if we have both __repr__() or __str__(), str() will have preference.
# print(o) --o is object of any class. if we have __str__() it will be called , if not __repr__() will be called.


# example of container functions
x= (1,2,3,4,5)
y= reversed(x) #returns an iterator
print (x)
print(y) #<reversed object at 0x0000020317467D60>

y=list(reversed(x))
print(y) #[5, 4, 3, 2, 1]

s=sum(x)
s=sum(x,10) #25
m=max(x)
n=min(x)
#any(x) returns True if any one of the element is true
# all(x) returns True if all of the elememts are true

x=(1,2,3,4,5)
y=(6,7,8,9)
z= zip(x,y)
for a,b in z:
    print(f'{a} - {b}')
#((1,6),(2,7),(3,8),(4,9))
x= ('cat','dog')
for i,v in enumerate(x): print(f'{i}:{v}')
#0:cat
#1:dog
