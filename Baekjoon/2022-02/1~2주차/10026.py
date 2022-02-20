import sys 
from copy import deepcopy 
from collections import deque

def mysolution():
    sys.setrecursionlimit(1000000*10)
    input = sys.stdin.readline
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    
    no, yes = 0, 0 
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    def no_dfs(i, j, check):
        _board[i][j] = '0'
        for k in range(4):
            _i, _j = i+dx[k], j+dy[k]
            if 0<=_i<n and 0<=_j<n and _board[_i][_j] == check:
                no_dfs(_i, _j, check)
        
    _board = deepcopy(board)
    for i in range(n):
        for j in range(n):
            if _board[i][j] in 'RGB':
                no += 1
                no_dfs(i, j, _board[i][j])
                
    def yes_dfs(i, j, check):
        _board[i][j] = '0'
        for k in range(4):
            _i, _j = i+dx[k], j+dy[k]
            if 0<=_i<n and 0<=_j<n:
                if (check == 'R' or check == 'G') and (_board[_i][_j] == 'R' or _board[_i][_j] == 'G'):
                    yes_dfs(_i, _j, _board[_i][_j])
                elif _board[_i][_j] == check:
                    yes_dfs(_i, _j, check)
                
    _board = deepcopy(board)
    for i in range(n):
        for j in range(n):
            if _board[i][j] in 'RGB':
                yes += 1
                yes_dfs(i, j, _board[i][j])
                
    print(no, yes)
        
def solution():
    input = sys.stdin.readline
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    copy = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 'R' or board[i][j] == 'G':
                copy[i][j] = 1
            else:
                copy[i][j] = 2
    
    def dfs(i, j, v, arr):
        q = deque([[i, j]])
        arr[i][j] = '0'
        while q:
            a, b = q.popleft()
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if 0 <= x < n and 0 <= y < n and arr[x][y] == v:
                    q.append([x, y])
                    arr[x][y] = '0'
    
    no, yes = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] != '0':
                no += 1
                dfs(i, j, board[i][j], board)
            if copy[i][j] != '0':
                yes += 1
                dfs(i, j, copy[i][j], copy)
     
    print(no, yes)

if __name__=='__main__':
    solution()