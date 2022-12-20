#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 120
y = 42

if x < y:
    print('x < y: x is {} and y is {}'.format(x, y))
elif x > y:
    print('x>y: x is {} and y is {}'.format(x,y))
else:
    print('else')

if x < y: print('x < y: x is {} and y is {}'.format(x, y)) #this will also work

#python doesnt have case and switch
#python 3.10 has match and case: https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/
