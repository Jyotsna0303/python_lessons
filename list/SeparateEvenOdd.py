#!bin/env python3
#input is a list and output should be two lists one having even and other odd

def separateEvenOdd(l):
    even=[]
    odd=[]
    for x in l:
        if x%2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even,odd

def separateEvenOddUsingComprehension(l):
    even=[x for x in l if x%2 ==0]
    odd=[x for x in l if x%2 !=0]
    return even,odd


def main():
    even, odd = separateEvenOdd([1,2,4,5,3,6,7])
    print(even)
    print(odd)
    print(type(even)) #<class 'list'>


if __name__=='__main__': main()
