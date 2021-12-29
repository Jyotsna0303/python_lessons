#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    kitten(5,6)

def kitten(a,b,c=0): #default arguments should come after other arguments otherwise Syntaxerror
    print('Meow.')

if __name__ == '__main__': main()


# __name__ is a special variable will return the name of the current module.
#__main__ is a special value which tells that this is not imported this the main file.
# all functions returns value in python. If we have not defined the value it will return None.

# Looks like Call by value in python but it looks like call by value.
# so the reference is passed id(argument) would be same in both of the methods(caller and calling)
# in case of the immutable object the value of the argument if changed in calling method wont be visible in caller method
# in case of mutable change would be visible

#so looks like call by value with immutable objects(int, str, tuple)
# and call by reference in case of mutable objects

# Few properties of functions in python
# A function is an instance of the Object type. Treat function as an object
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists, …

#Treat function as an object
def shout(text):
    return text.upper()


print(shout('Hello'))

yell = shout

print(yell('Hello'))

#Passing the function as an argument
# Python program to illustrate functions
# can be passed as arguments to other functions
def shout(text):
    return text.upper()


def whisper(text):
    return text.lower()


def greet(func):
    # storing the function in a variable
    greeting = func("""Hi, I am created by a function passed as an argument.""")
    print(greeting)


greet(shout)
greet(whisper)

#Returning functions from another function.
def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print(add_15(10))