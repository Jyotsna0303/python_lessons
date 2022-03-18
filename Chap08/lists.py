#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print_list(game) #Rock Paper Scissors Lizard Spock
    print(game) #['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    print(game[0])
    print(game[1:4]) #['Paper', 'Scissors', 'Lizard']
    #we can use step in indexes as range() too
    print(game[1:5:2])# ['Paper', 'Lizard']
    print(','.join(game)) #join is a method which takes a sequence and returns a string combining all elements of sequence
    print(len(game))
    #search for index with value
    i=game.index('Paper')#ValueError if value is not present in list
    print(i)
    i=game.index('Paper',1,5) #it will check from index 1 to 4, 1= start, 5 is end

    # modify the list
    game.append('Computer')
    game.insert(0,'Mouse')
    game.remove('Mouse') #ValueError if element not present 
    x=game.pop() #pop() returns the last value and removes from the list
    x=game.pop(3)
    del game[3]
    del game[1:3]
    del game[1:5:2]

    #few other methos
    game.count('Computer'); #return 1, counts the occurence of elements in list.
    print(max(game))
    print(min(game))
    print(sum(game))
    print(game.sort()) #by default it is in increasing order
    print(game.reverse())
    
    #max(), min(),sum(),sort() these method wont work if there are mixed items inside the list
    
    #tuple is same as list, but it is immutable. modification methods wont be available
def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()



if __name__ == '__main__': main()

