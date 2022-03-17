import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    dp = [1e9]*(n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = min(dp[i-1]+1, (i//3)+dp[i%3])
        
    if dp[n]%2==0:
        print('CY')
    else:
        print('SK')
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    if n % 2 == 0:
        print('CY')
    else:
        print('SK')
        
if __name__=='__main__':
    mysolution()