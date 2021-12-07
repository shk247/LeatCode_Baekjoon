import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    floor = [int(input()) for _ in range(n)]
    now = 0
    total = 0 
    while now < len(floor):
        total += floor[now]
         
def solution():
    input = sys.stdin.readline
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    dp = [0 for _ in range(n)]
    
    if n<3:
        print(sum(arr))
        return
    
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0]+arr[2], arr[1] + arr[2])
    for i in range(3,n):
        dp[i] = max(arr[i]+dp[i-2], dp[i-3]+arr[i-1]+arr[i])
    print(dp[n-1])

if __name__=='__main__':
    mysolution()