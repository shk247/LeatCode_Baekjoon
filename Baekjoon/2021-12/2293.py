import sys 

def mysolution():
    input = sys.stdin.readline
    n,k = map(int, input().split())
    values = [int(input()) for i in range(n)]
    minimum = 1e9
    
    
def solution():
    input = sys.stdin.readline
    n,k = map(int, input().split())
    values = [int(input()) for i in range(n)]
    dp = [0 for i in range(k+1)]
    dp[0] = 1 
    
    for value in values:
        for j in range(value, k+1):
            if j-value>=0:
                dp[j] += dp[j-value]
                print('value=',value,'j=',j,'dp=',dp)
                
    print(dp[k])

if __name__=='__main__':
    solution()