import sys 

def mysolution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins = list(set(coins))

    num = [1e9]* (k+1) 
    num[0] = 0
    
    for coin in coins:
        for i in range(coin, k+1):
            if i-coin>=0 and num[i-coin] != 1e9:
                num[i] = min(num[i-coin] + 1, num[i])
                
    if num[k] == 1e9:
        print(-1)
    else:
        print(num[k])
                    
                
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()