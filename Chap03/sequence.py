#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# sequences in python: list, tuple and dictionary

x = [ 1, 2, 3, 4, 5 ] #list
x[2]= 42
for i in x:
    print('i is {}'.format(i))

#list is mutable, we can access with index.
#tuple is not mutable. tuple works same as list except we cannot change content of tuple.

x= (1, 2, 3, 4,5) #tuple
print(type(x)) #class tuple
#x[2]=42 #give error "tuple object does not support item assignment"
for i in x:
    print('i is {}'.format(i))


#create sequence using range function
x = range(4)
print(type(x)) # type= class range. range is also not mutable.
x = range(0, 50, 5) # 0= first, 50= end, 5= step

# list from range()
x = list(range(5))
print(type(x)) #class list

# dictionary
# dictionary is mutable
x= {'one':1, 'two':2}
print(type(x)) # class dict
for i in x:
    print('i is {}'.format(i)) #i is one i is two # this will print keys

for k,v in x.items(): # return two tuples one with key and one with item.
    print('k:{}, v:{}'.format(k,v))



