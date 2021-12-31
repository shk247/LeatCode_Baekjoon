import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    check = [0]
    for i in range(len(nums)-1):
        if nums[i]>nums[i+1]:
            check.append(check[-1]+1)
        else:
            check.append(check[-1])
    check.append(0)
            
    q = int(input())
    for _ in range(q):
        a, b = map(int, input().split())
        print(check[b-1]-check[a-1])
    
def solution():
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [0]*N
    for i in range(1,N):
        if arr[i-1] < arr[i]:
            dp[i] = dp[i-1]
        else:
            dp[i] = dp[i-1] + 1
    Q = int(input())
    for _ in range(Q):
        x, y = map(int, input().split())
        print(dp[y-1] - dp[x-1])

if __name__=='__main__':
    solution()