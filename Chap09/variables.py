#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

class Animal:
    x=[1,2,3] #this is associated with class not with a single object
    def __init__(self, **kwargs):
        self._type = kwargs['type'] if 'type' in kwargs else 'kitten' #object variables
        self._name = kwargs['name'] if 'name' in kwargs else 'fluffy'
        self._sound = kwargs['sound'] if 'sound' in kwargs else 'meow'

    def type(self, t = None):
        if t: self._type = t # '_' in _type is a convention in python which tells that this data should not be accessed directly.(like private variables of other languages.)
        return self._type

    def name(self, n = None):
        if n: self._name = n
        return self._name

    def sound(self, s = None):
        if s: self._sound = s
        return self._sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

def main():
    a0 = Animal(type = 'kitten', name = 'fluffy', sound = 'rwar')
    a1 = Animal(type = 'duck', name = 'donald', sound = 'quack')
    print(a0)
    print(a1)
    a0.x[0]=4
    print(a1.x)#[4, 2, 3]

if __name__ == '__main__': main()

#the object variables are encapsulated
#the class variables are not encapsulated.
#we should keep data which wo dont want to change for every object. And we want should be created only once for a class.
#we should chose class variable as immutable