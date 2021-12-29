#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import sys

def main():
    print('Hello, World.')
    try:
        x = int('foo') #ValueError: invalid literal for int() with base 10: 'foo'
    except ValueError:
        print(f'ValueError caught: {sys.exc_info()}') #sys will give  more details about the error
    except :
        print('Unknown error') #Default
    else:
        print('good job') #will be executed if there are no exceptions
    #different exceptions ZeroDivisionError


if __name__ == '__main__': main()

#runtime reporting error mechanism.= exceptions