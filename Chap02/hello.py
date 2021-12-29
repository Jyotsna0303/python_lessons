#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x=42
print('Hello, World. {}'.format(x)) #format is method of string class
s='Hello, World. {}'.format(x)
print(s)
print(f'Hello, World.{x}') #f string is implemented by calling format() internally.

#all print will print same value
