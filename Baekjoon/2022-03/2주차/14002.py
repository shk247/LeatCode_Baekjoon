import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [1]*(n)
    pre = nums[0] 
    print(nums[0], end=' ')
    for i in range(1, n):
        if pre<nums[i]:
            dp[i] = dp[i-1]+1
            pre=nums[i]
            print(nums[i], end=' ')
        else:
            dp[i] = dp[i-1]
            
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [1]*(n)
    for i in range(1, n):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
                
    maximum = max(dp)
    print(maximum)
    
    answer = []
    for i in range(n-1, -1, -1):
        if dp[i]==maximum:
            answer.append(nums[i])
            maximum-=1
            
    answer.sort()
    
    print(' '.join(map(str, answer)))
    
    
if __name__=='__main__':
    solution()