#every number appeares even number of time, only one number in the list appears odd number of time.
#find that number

def findOddOccurence(l):
    res=None
    for x in l:
        c=l.count(x)
        if c%2!=0:
            res=x
            break
    return res
def main():
    print(findOddOccurence([2,2,2,1,1,1,3,3,3,3,4,4]))

if __name__=='__main__':main()