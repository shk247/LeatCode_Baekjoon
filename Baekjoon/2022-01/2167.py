import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    k = int(input())
    
    for _ in range(k):
        i, j, x, y = map(int, input().split())
        i, j, x, y = i-1, j-1, x-1, y-1 
        # min_x, max_x = min(i,x), max(i,x)+1
        # min_y, max_y = min(j,y), max(j,y)+1
        ans = 0 
        for a in range(i, x+1):
            for b in range(j, y+1):
                ans += board[a][b]
        print(ans)
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = board[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
    
    k = int(input())
    for _ in range(k):
        i, j, x, y = map(int, input().split())
        print(dp[x][y]-dp[i-1][y]-dp[x][y-1]+dp[i-1][j-1])

if __name__=='__main__':
    mysolution()