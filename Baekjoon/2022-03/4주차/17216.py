import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [0]*n
    
    for i in range(n):
        for j in range(i+1, n):
            if nums[i]>nums[j]:
                dp[j] = max(dp[j], dp[i]+nums[j])
    
    print(max(dp))
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    dp = nums[:]
    
    for i in range(n):
        for j in range(i):
            if nums[i]<nums[j]:
                dp[i] = max(dp[i], dp[j]+nums[i])
    
    print(max(dp))

if __name__=='__main__':
    solution()