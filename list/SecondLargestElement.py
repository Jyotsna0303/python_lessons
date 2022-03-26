#time complexity theta(n), only one traversal
def getSecondLargestElement(l):
    if len(l)<=1:
        return None
    larg=l[0]
    slarg=None

    for x in l[1:]:
        if x>larg:
            slarg=larg
            larg=x
        elif x!=larg:
            if slarg==None or slarg<x:
                slarg=x
    return slarg

def main():
    print(getSecondLargestElement([0,2,1,5,67,89]))

if __name__=='__main__':main()
