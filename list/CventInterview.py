#Given a string of length N with only letters A and B, find minimum number of letters to be deleted
# so that the string has all A letters before B.
#input= 'AABBABB', o/p= 1, result string=AABBBB

def getMinNumber(S):
    result=list(S)
    #result=[]
   # print(result)
    i=1
    count=0
    while i!=len(result):
        if result[i]=='A':
            if result[i-1]=='B' and result[i+1]=='A':
                result.pop(i-1)
                count+=1
        elif result[i]=='B':
            if result[i - 1] == 'A' and result[i + 1] == 'A':
                result.pop(i)
                count += 1
            elif result[i-1]=='B' and result[i+1]=='A':
                result.pop(i+1)
                count += 1
    return count



def main():
    print(getMinNumber('AABBABB'))

if __name__=='__main__':main()


