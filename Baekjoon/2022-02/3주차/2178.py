import sys 
from collections import deque

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(n)]
    dp = [[0]*(m+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i-1][j-1] == 1:
                pass
    print(dp)
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append([0, 0])
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<m and board[nx][ny]==1:
                board[nx][ny] += board[x][y]
                q.append([nx, ny])
                
    print(board[n-1][m-1])
    
if __name__=='__main__':
    solution()