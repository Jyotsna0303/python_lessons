#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

# sequences in python: list, tuple and dictionary

x = [ 1, 2, 3, 4, 5 ] #list
x[2]= 42
for i in x:
    print('i is {}'.format(i))

#for finding index we can use index() method

 
#The enumerate() function in Python is used to iterate over a sequence (like a list, tuple, or string) while keeping track of the index.
x = ['a', 'b', 'c', 'd']

for index, value in enumerate(x):
    print(f"Index: {index}, Value: {value}")
#for multiple occurences
x = [10, 20, 42, 30, 42, 50]
target = 42

indices = [i for i, value in enumerate(x) if value == target] #List comprehension
print(indices) #[2,4] 

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



