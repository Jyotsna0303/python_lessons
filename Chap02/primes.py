#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def isprime(n):
    if n <= 1:
        return False
    for x in range(2, n): #range function will give values 2 to n, not including n. range(100) will return 0 to 100 not including 100
        if n % x == 0:
            return False
    else:
        return True

n = 5
if isprime(n):
    print(f'{n} is prime')
else:
    print(f'{n} not prime')

