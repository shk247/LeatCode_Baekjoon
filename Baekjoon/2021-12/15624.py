import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    p = [0, 1] + [0]*(n-1)
    for i in range(2,n+1):
        p[i] = p[i-1]+p[i-2]
    print(p[n]%1000000007)
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    a, b = 0, 1
    for i in range(n):
        a, b = (a+b)%1000000007, a%1000000007
    print(a)

if __name__=='__main__':
    mysolution()