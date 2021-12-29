#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten('meow', 'grrr', 'purr')
    #we can call another way
    x=('meow', 'grrr', 'purr')
    kitten(*x) # we can use list, tuple or any other collection

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()
