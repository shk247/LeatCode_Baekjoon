import sys 

def mysolution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    stuff = [list(map(int, input().split())) for _ in range(n)]
    
def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    stuff = [[0, 0]]
    stuff.extend(list(map(int, input().split())) for _ in range(n))
    dp = [[0]*(k+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1, k+1):
            w, v = stuff[i][j]
            if j<w:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
    
    print(dp[n][k])

if __name__=='__main__':
    mysolution()