import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    cnt = 0 
    while n!=1:
        print('n=',n,'cnt=',cnt)
        if n%3==0:
            n -= 1
            cnt +=1
            if n%2==0:
                n //= 2
                cnt+=1
        elif n%2==0:
            n -= 1
            cnt +=1
            if n%3==0:
                n //= 3
                cnt+=1
        else:
            n-=1
            cnt+=1
    print(cnt)
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    d = [0]*(n+1)
    
    for i in range(2,n+1):
        d[i] = d[i-1] + 1
        if i%3 == 0:
            d[i] = min(d[i], d[i//3]+1)
        if i%2 == 0 :
            d[i] = min(d[i], d[i//2]+1)
    
    print(d[n])

if __name__=='__main__':
    mysolution()