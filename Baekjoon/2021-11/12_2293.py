
def mysolution():
    n, k = list(map(int, input().split()))
    values = [int(input()) for _ in range(n)]
    

def solution():
    n, k = list(map(int, input().split()))
    values = [int(input()) for _ in range(n)]
    dp = [0 for i in range(k+1)]
    dp[0] = 1
    
    for i in values:
        for j in range(i, k+1):
            if j-i>=0:
                dp[j] += dp[j-i]
                
    print(dp[k])
    
if __name__ == '__main__':
    mysolution()
    
    