import sys 
from collections import deque

def mysolution():
    input = sys.stdin.readline
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    n = int(input())
    
    board = [list(input().strip()) for _ in range(n)]

    cnt = 0 
    answer = []
    
    def dfs(x, y):
        nonlocal cnt
        board[x][y] = '0' 
        cnt += 1
        for i in range(4):
            _x, _y = x+dx[i], y+dy[i]
            if 0<=_x<n and 0<=_y<n and board[_x][_y]=='1':
                dfs(_x, _y)
                
    for i in range(n):
        for j in range(n):
            if board[i][j]=='1':
                dfs(i, j)
                answer.append(cnt)
                cnt=0
                
    print(len(answer))
    answer.sort()
    for a in answer:
        print(a)
        
def mysolution_bfs():
    input = sys.stdin.readline
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]

    cnt = 0 
    answer = []
    q = deque()
    
    for i in range(n):
        for j in range(n):
            if board[i][j]=='1':
                q.append([i,j])
                board[i][j] = '0'
                while q:
                    cnt+=1
                    x, y = q.popleft()
                    for k in range(4):
                        _x, _y = x+dx[k], y+dy[k]
                        if 0<=_x<n and 0<=_y<n and board[_x][_y]=='1':
                            board[_x][_y] = '0'
                            q.append([_x, _y])
                answer.append(cnt)
                cnt=0
    print(len(answer))
    answer.sort()
    for a in answer:
        print(a)    
                
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution_bfs()