def reverseAList(l):
     l.reverse()
     return l



#custom reverse in one traversal
def customReverse(l):
    start=0
    end=len(l)-1
    while start<end:
        l[start],l[end]=l[end],l[start] #swapping like this is possible in python. no need of temp variable
        start+=1
        end-=1
def main():
    print(reverseAList([2,5,6,90]))
    l=[2,5,6,90]
    # return l.reverse() will return NONE. Because reverse will act on the current list it will not return a new list.
    newl=list(reversed(l))
    newl1=l[::-1]
    # for a new list having reversed element

    # another way is using slicing
    newl1 = l[::-1]
    l1 = [2, 4, 5 ]
    customReverse(l1)
    print(l1)

#reverse() is only avalaile with list as it is mutable.
#reverse not avaliable for set and tuple.
#slicing and reversed() can be used for immutable and mutable both.



if __name__=='__main__':main()