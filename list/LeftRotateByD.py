#d is the number by which we have to left rotate
def getLeftRotateByD(l,d):
    #l=l[d:] +l[:d]
    # or

    #overall time complexity theta(nd)
    for i in range(0,d):
        l.append(l.pop(0)) #pop(0) is theta(n) operation, append() is constant time
    print (l)

def LeftRotationUsingReverse(l,d):
    n=len(l)
    reverseList(l,0,d-1) #theta(d)
    reverseList(l,d,n-1) #theta(n-d)
    reverseList(l,0,n-1) #theta(n)
    #total= theta(2n)=theta(n)
    #ayxillaryspace=theta(1)

def reverseList(l,start,end):
    while start<end:
        l[start],l[end]=l[end],l[start]
        start=start+1
        end=end-1


def main():
    getLeftRotateByD([35,6,5,3,2,34], 3)

if __name__=='__main__':main()