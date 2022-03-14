import sys 

def mysolution():
    input = sys.stdin.readline
    price = int(input())
    coins = [1, 2, 5, 7]
    dp = [0]*(price+1)
    
    
def solution():
    input = sys.stdin.readline
    price = int(input())
    coins = [7, 5, 2, 1]
    dp = [100001]*(price+1)
    dp[0] = 0 
    
    for n in range(1, price+1):
        for coin in coins:
            if n>=coin and dp[n-coin]+1<dp[n]:
                dp[n]=dp[n-coin]+1
                
    price(dp[price])

if __name__=='__main__':
    mysolution()