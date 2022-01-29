import sys 

def mysolution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    for i in range(1, k+1):
        for coin in coins:
            if i-coin>=0:
                dp[i] += dp[i-coin]
    print(dp)
    
def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    dp = [0 for _ in range(k+1)]
    dp[0] = 1
    for coin in coins:
        for j in range(coin, k+1):
            if j-coin>=0:
                dp[j] += dp[j-coin]
    print(dp[k])
    
if __name__=='__main__':
    mysolution()