import sys 
from collections import deque

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append([0,0])
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            _x, _y = x+dx[k], y+dy[k]
            if 0<=_x<n and 0<=_y<m and board[_x][_y]==1:
                board[_x][_y] = board[x][y]+1 
                q.append([_x,_y])
    
    print(board[n-1][m-1])
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()