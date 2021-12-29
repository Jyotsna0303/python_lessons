#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

s = 'This is a long string with a bunch of words in it.'
print(s.split()) #returns a list splitting on space.

l=s.split()
s2=':' .join(l) #returns a string combined with all elements of list with :
print(s2) #This:is:a:long:string:with:a:bunch:of:words:in:it.