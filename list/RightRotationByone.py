
def rightRotation(l):
    l=l[-1:]+l[0:len(l)-1]
    print(l)

def main():
    rightRotation([23,45,4,4,7,9])

if __name__=='__main__':main()