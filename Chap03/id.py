#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

#id()  return the identity of an object. This identity has to be unique and constant for this object during the lifetime. Two objects with non-overlapping lifetimes may have the same id() value
# If we relate this to C, then they are actually the memory address, here in Python it is the unique id. This function is generally used internally in Python.
i = (1,'four', 3.0,[1,'two'])
j = (1,'four', 3.0,[1,'two'])
print(id(i))
print(id(j))
#the above two ids will be different

a=(1,'four',3.0)
b=(1,'four',3.0)
print(id(a))
print(id(b))
#the above two ids will be same

x=[1,'four',3.0]
y=[1,'four',3.0]
#the above two ids will be different

print(id(i[1]))
print(id(j[1]))
 #above two ids will be same.


 #is operator
if i[0] is j[0]:
    print('they are same object') #true

if i is j:
    print('i and j are same object')
else:
    print('i and j  are not same object')#true

a= 5
b=5
print(id(a))
print(id(b))
if a is b:
    print("a and b are same object") #true
else:
    print("a and b are not same object") 




#isinstance() method to check if object of same

if isinstance(i,tuple):
    print('i is tuple') #true
elif isinstance(i,list):
    print('i is list')

