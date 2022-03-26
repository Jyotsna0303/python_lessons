def leftRotateByOne(l):
    #use direct method
   # l=l[1:]+l[0] #this will give error TypeError: can only concatenate list (not "int") to list
    l = l[1:] + l[0:1]
    #or
    #l.append(l.pop(0))
    print(l)

def leftRotateCustom(l):
    x=l[0]
    n=len(l)
    for i in range(1,n):
        l[i-1]=l[i]
    l[n-1]=x
    print(l)


def main():
   # leftRotateByOne([20,30,40,50])
    leftRotateCustom([20,40,50])
if __name__=='__main__': main()