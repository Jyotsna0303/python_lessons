#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    infile = open('lines.txt', 'rt')
    outfile = open('lines-copy.txt', 'wt')
    for line in infile:
        print(line.rstrip(), file=outfile)
        #outfile.writelines(line)
        print('.', end='', flush=True)
    outfile.close() #closing the file while writing. but we can miss the data.
    infile.close() # not so imp because file will be closed when we exit the function
    print('\ndone.')

if __name__ == '__main__': main()
