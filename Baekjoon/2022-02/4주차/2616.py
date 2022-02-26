import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    small_n = int(input())
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    k = int(input())
    dp = [[0]*(n+1) for _ in range(4)]
  
    total = [0]
    for i in range(1, n+1):
        total.append(total[i-1]+nums[i])

    for i in range(1, 4):
        for j in range(i*k, n+1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j-k]+total[j]-total[j-k])
            
    print(dp[3][n])

if __name__=='__main__':
    solution()