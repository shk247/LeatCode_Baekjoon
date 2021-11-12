def mysolution():
    m = int(input())
    n = int(input())
    
    minority = [False,False] + [True]*(n-1)
    
    for i in range(2, n+1):
        if minority[i] == True:
            for j in range(2*i,n+1,i):
                minority[j] = False
    
    answer = [i for i in range(m,n+1) if minority[i]==True]
    
    if answer:
        print(sum(answer))
        print(answer[0])
    else:
        print(-1)    
    
if __name__=='__main__':
    mysolution()