#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    seq = range(11)
    seq2 = [x * 2 for x in seq] #comprehension =list created by another list.
    seq3 = [x for x in seq if x%3 !=0] #2nd example of comprehension
    seq4 = [(x, x**2) for x in seq]
    seq5= {x: x*2 for x in seq } #dictionary
    print_list(seq)
    print_list(seq2)
    print_list(seq4) #(0, 0) (1, 1) (2, 4) (3, 9) (4, 16) (5, 25) (6, 36) (7, 49) (8, 64) (9, 81) (10,100)


def print_list(o):
    for x in o: print(x, end = ' ')
    print()

if __name__ == '__main__': main()

#