#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

animals = ( 'bear', 'bunny', 'dog', 'cat', 'velociraptor' )

for pet in animals:
    if pet=='dog' : continue # Skip 'dog' and move to the next iteration
    print(pet)
else : #In Python, a for loop can have an else block, which is executed only if the loop completes normally (i.e., without encountering a break).
    print('This is all')
#bear,bunny,cat, velociraptor, This is all.

for pet in range(5): #prints 0,1,2,3,4
    print(pet)
