import sys 
from collections import deque

def mysolution_dfs():
    input = sys.stdin.readline
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    
    answer = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    def dfs(i, j):
        global cnt
        cnt += 1
        board[i][j] = '0'
        for k in range(4):
            _i, _j = i+dx[k], j+dy[k]
            if 0<=_i<n and 0<=_j<n and board[_i][_j] == '1':
                dfs(_i, _j)
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == '1':
                global cnt
                cnt = 0 
                dfs(i,j)
                answer.append(cnt)
                
    answer.sort()
    
    print(len(answer))
    for a in answer:
        print(a)

def mysolution_bfs():
    input = sys.stdin.readline
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    
    answer = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == '1':
                q = deque([[i, j]])
                board[i][j] = 0
                cnt = 0 
                while q:
                    x, y = q.popleft()
                    cnt+=1
                    for k in range(4):
                        _x, _y = x+dx[k], y+dy[k]
                        if 0<=_x<n and 0<=_y<n and board[_x][_y] == '1':
                            q.append([_x, _y])
                            board[_x][_y] = 0
                answer.append(cnt)
                
    answer.sort()
    
    print(len(answer))
    for a in answer:
        print(a)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution_bfs()