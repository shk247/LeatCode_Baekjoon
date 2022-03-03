import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-101] * (m+1) for _ in range(n+1)]
    
    dx = [-1, 0]
    dy = [0, -1]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            tmp = -101
            for k in range(2):
                nx, ny = i+dx[k], j+dy[k]
                if 0<=nx<n and 0<=ny<m:
                    tmp = max(tmp, dp[nx][ny])
            dp[i][j] = nums[i-1][j-1]
            if tmp != -101:
                dp[i][j] += tmp 
            
    print(dp)
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(n)]
    dp = [[-101] * (m) for _ in range(n)]
    left = [[-101] * (m) for _ in range(n)]
    right = [[-101] * (m) for _ in range(n)]
    
    dp[0][0] = nums[0][0]
    for i in range(1, m):
        dp[0][i] = dp[0][i-1] + nums[0][i]
        
    for i in range(1, n):
        # 왼->오
        left[i][0] = dp[i-1][0] + nums[i][0]
        for j in range(1, m):
            left[i][j] = max(dp[i-1][j], left[i][j-1]) + nums[i][j]
        
        # 오->왼
        right[i][m-1] = dp[i-1][m-1] + nums[i][m-1]
        for j in range(m-2, -1, -1):
            right[i][j] = max(dp[i-1][j], right[i][j+1]) + nums[i][j]
        
        for j in range(m):
            dp[i][j] = max(left[i][j], right[i][j])
            
    print(dp[n-1][m-1])
    
if __name__=='__main__':
    solution()