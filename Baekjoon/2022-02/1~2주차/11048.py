import sys 
import copy

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    original = copy.deepcopy(board)
    
    dx = [1, 0, 1]
    dy = [0, 1, 1]
    
    for i in range(n):
        for j in range(m):
            for k in range(3):
                _i, _j = i+dx[k], j+dy[k]
                if 0<=_i<n and 0<=_j<m:
                    board[_i][_j] = max(board[_i][_j], board[i][j]+original[_i][_j])
                    
    print(board[n-1][m-1])
    
def solution():
    input = sys.stdin.readline
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(m+1)] * (n+1)
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = board[i-1][j-1] + max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
            
    print(dp[n][m])

if __name__=='__main__':
    solution()