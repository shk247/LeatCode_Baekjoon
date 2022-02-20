import sys 

def mysolution():
    input = sys.stdin.readline
    a = input().strip()
    b = input().strip()
    n = len(a)
    m = len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i] == b[i]:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    print(dp[n][m])
            
def solution():
    input = sys.stdin.readline
    a = input().strip()
    b = input().strip()
    n = len(a)
    m = len(b)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if a[i] == b[i]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    print(dp[n][m])
    
if __name__=='__main__':
    mysolution()