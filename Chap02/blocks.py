#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    z=112
    print('x < y: x is {} and y is {}'.format(x, y))
print(z) #this will print value of z because block doesnt define the scope of variable. Function,objects, modules define scope