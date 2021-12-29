#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def function(n):
    print(n)

function(47)

def function2(x = 1):
    print(x)

function2(5) #5 will be printed
function2() #default value will be printed

#all functions return value in python. So if function is not returning anything by defualt it will return 'None'
a=function(47)
print(a)#print None