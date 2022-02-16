import sys 

def mysolution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    dp = [1e9] * (k+1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, k+1):
            if i-coin>=0:
                dp[i] = min(dp[i], dp[i-coin]+1)
    
    if dp[k] == 1e9:
        print(-1)
    else:
       print(dp[k])
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()