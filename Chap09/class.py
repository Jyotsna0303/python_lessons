#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    def quack(self):#self is not a keyword. But first argument is considered as the reference to self object. self is a convention.
        print(self.sound) #self shows that this is a method and not a plain function

    def move(self):
        print(self.movement)

def main():
    donald = Duck()
    donald.quack()
    donald.move()

if __name__ == '__main__': main()
