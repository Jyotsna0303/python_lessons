#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    a = set("We're gonna need a bigger boat.")
    b = set("I'm sorry, Dave. I'm afraid I can't do that.")
    print(a)  # {'a', 'o', 'i', 'g', '.', 'd', 'n', 't', 'b', 'r', "'", ' ', 'e', 'W'}
    print(sorted(a)) #[' ', "'", '.', 'W', 'a', 'b', 'd', 'e', 'g', 'i', 'n', 'o', 'r', 't']
    #sorted method returns list
    print_set(a) #{Wngodeab'. rti}
    print_set(b) #{nsyfm ,rDe.vodatiIh'c}
    #print elements of a not present in b
    print_set(a-b)

    #print elements present in a or b
    print_set(a | b)

def print_set(o):
    print('{', end = '')
    for x in o: print(x, end = '')
    print('}')

if __name__ == '__main__': main()

#set is unordered list of unique values {1, 2, 3,4,5}