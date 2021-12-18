import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    
    fibo = [1, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1]+fibo[i-2]+1)
        
    print(fibo[n]%1000000007)

    
def solution():
    input = sys.stdin.readline
    n = int(input())
    
    num = [1, 1]
    for _ in range(n-1):
        num.append(num[-1]+num[-2]+1)
    
    print(num[-1]%1000000007)

if __name__=='__main__':
    solution()