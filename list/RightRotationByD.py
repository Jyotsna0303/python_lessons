
def rightRotationByD(l,d):
    #slicing
    l=l[-(len(l)-d-1):]+l[:len(l)-d]
    print(l)

def rightRotationUsingReverse(l,d):
    n=len(l)
    reverseList(l,0,n-1) #theta(n)
    reverseList(l,0,d-1) #theta(d)
    reverseList(l,d,n-1) #theta(n-d)
    #total= theta(2n)=theta(n)
    #ayxillaryspace=theta(1)
    print(l)

def reverseList(l,start,end):
    while start<end:
        l[start],l[end]=l[end],l[start]
        start=start+1
        end=end-1
def main():
    #rightRotationByD([3,5,6,78,90],2)
    rightRotationUsingReverse([3,5,6,7,8],2)

if __name__=='__main__': main()