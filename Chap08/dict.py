#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    animals = { 'kitten': 'meow', 'puppy': 'ruff!', 'lion': 'grrr',
        'giraffe': 'I am a giraffe!', 'dragon': 'rawr' }
    #another way
    animals1 = dict(kitten='meow', puppy='ruff!', lion= 'grrr',
        giraffe='I am a giraffe!', dragon= 'rawr')
    print_dict(animals)

    print(animals['lion']) #KeyError if key doesnt exists we can use get() so that we dont get error
    print(animals.get('lion')) #returns None if key doesnt exists
    animals['lion'] = 'roar'
    print('lion' in animals)  #True #check if key exists in dict.

def print_dict(o):
    for x in o: print(f'{x}: {o[x]}')

    # using items()
    for k, v in o.items(): print(f'{k} : {v}')

    #keys of dict
    for k in o.keys(): print(k)

   #values of dict
    for v in o.values(): print(v)

if __name__ == '__main__': main()

#keys should be immutable