import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [0]*(n)

    for i in range(n):
        cnt = 1
        max_num = nums[i]
        for j in range(i+1, n):
            if nums[j]>max_num:
                cnt += 1
                max_num = nums[j]
        dp[i]=cnt 
        
    print(dp)
    print(max(dp))
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [1]*(n)

    for i in range(n):
        tmp = 0 
        for j in range(i):
            if nums[i]>nums[j]:
                tmp = max(tmp, dp[j])
        dp[i]+=tmp

    print(dp)
    print(max(dp))

if __name__=='__main__':
    solution()