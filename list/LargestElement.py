def getLargestElement(l):
    return max(l)


#time complexity=theta(n)
def getLargestElementCustom(l):
    if not l:
        return None  #if list is empty
    else:
        res=l[0]
        for i in range(1,len(l)):
            if l[i]>res:
                res=l[i]
        return res

def main():
    print(getLargestElementCustom([1,5,6,7,10,4,59]))
if __name__=='__main__':main()

