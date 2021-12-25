import sys 

def mysolution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins.sort(reverse=True)
    cnt = 0 
    for coin in coins:
        if k-coin<0:
            break
        
        k, r = divmod(k,coin)
        cnt += r
    if cnt:
        print(cnt)
    else:
        print(-1)
    
def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    dp = [1e9] * (k+1)
    dp[0] = 0
    for i in range(1, k+1):
        tmp = []
        for coin in coins:
            if i-coin >= 0 and dp[i-coin] != -1:
                tmp.append(dp[i-coin]+1)
        if not tmp:
            dp[i] = -1
        else:
            dp[i] = min(tmp)
    print(dp[k])

if __name__=='__main__':
    mysolution()