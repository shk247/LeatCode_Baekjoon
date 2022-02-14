import sys 

def mysolution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    
    dp = [0] * (k+1)
    dp[0] = 1 
    
    for i in range(1, k+1):
        for coin in coins:
            if i%coin == 0:
                dp[i] += 1
                        
    print(dp[k])
    
def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    
    dp = [0] * (k+1)
    dp[0] = 1    
    
    for coin in coins:
        for i in range(coin, k+1):
            if i-coin>=0:
                dp[i] += dp[i-coin]
                
    print(dp[k])
           
if __name__=='__main__':
    mysolution()