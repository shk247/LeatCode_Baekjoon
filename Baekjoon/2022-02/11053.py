import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    answer = 0
    for i in range(n):
        cnt = 1
        tmp = nums[i]
        for j in range(i+1, n):
            if tmp<nums[j]:
                tmp = nums[j]
                cnt += 1
        answer = max(answer, cnt)
        
    print(answer)
            
def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    dp = [1]*n
    for i in range(n):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print(max(dp))
    
if __name__=='__main__':
    mysolution()