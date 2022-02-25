import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [1]*n
    
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    
    length = max(dp)            
    print(length)
    
    idx = 0
    for i in range(1, length+1):
        while dp[idx] != i:
            idx += 1
        print(nums[idx], end=' ')

if __name__=='__main__':
    solution()