#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    f = open('lines.txt')  #return a stream # f is an fileobject which is a iterator
    print(type(f)) #<class '_io.TextIOWrapper'>
    for line in f: #line is str
        print(line.rstrip()) #this method will strip any whitespace

if __name__ == '__main__': main()

#open('filepath') be default opens in read mode
#open('filepath', 'r') readmode
#open('filepath', 'w') write mode , if opened in write mode it replaces the whole content and erases the older content.
#if file doesnt exists 'w' mode will create it
# open('filepath','a') append mode, new content will be appended at end. This will not create file if not exists and will not replace the content.
#open('','r+') #open in both read and write
#open('','r+t') or open('','r+b') #b-- binary, t-- text
