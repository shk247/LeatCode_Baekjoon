import sys 

def mysolution():
    input = sys.stdin.readline
    k = int(input())
    x ='0'
    cnt = 0 
    
    while k>2**cnt:
        cnt+=1
        tmp = ''.join(['1' if x[i]=='0' else '0' for i in range(len(x))])
        x += tmp
    
    print(x[k-1])
    
def recursive(n):
    print("n=",n)
    if n==0:
        return 0
    if n==1:
        return 1
    if n%2:
        return 1-recursive(n//2)
    else:
        return recursive(n//2)
    
def solution():
    input = sys.stdin.readline
    k = int(input())
    print(recursive(k-1))
    

if __name__=='__main__':
    solution()