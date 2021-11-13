
def solution():
    n, k = list(map(int, input().split()))
    nums = [int(input()) for _ in range(n)]
    dp = [1e9]*(k+1)
    dp[0] = 0 
    for i in range(n):
        for j in range(nums[i], k+1):
            dp[j] = min(dp[j], dp[j-nums[i]]+1)
    
    return -1 if dp[-1] == 1e9 else dp[-1]
    
if __name__ == "__main__":
    print(solution())