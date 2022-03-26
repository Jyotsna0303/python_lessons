
#input a list and a number output a list having smaller elements from the list. Smaller than the input number
def getSmallerElements(l,num):
    res=[]
    for x in l:
        if x <num:
            res.append(x)
    return res

def getSmallerUSingComprehension(l,num):
    return [x for x in l if x<num]

def main():
    print(getSmallerElements([1,2,3,4,5,6,2], 3)) #[1, 2, 2]

if __name__=='__main__' : main()
