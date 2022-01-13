import sys 
from collections import deque

def mysolution():
    input = sys.stdin.readline
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    t = int(input())
    
    for _ in range(t):
        m, n, k = map(int, input().split())
        ans = 0 
        board = [['0' for _ in range(n)] for _ in range(m)]
        
        for _ in range(k):
            a, b = map(int, input().split())
            board[a][b] = '1'
        
        def dfs(i, j):
            board[i][j] = '0'
            for k in range(4):
                _i, _j = i+dx[k], j+dy[k]
                if 0<=_i<m and 0<=_j<n and board[_i][_j]=='1':
                    dfs(_i, _j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == '1':
                    dfs(i, j)
                    ans+=1
                    
        print(ans)
    
    
    
def solution():
    input = sys.stdin.readline
    t = int(input())
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
        
    def bfs(s, x, y):
            queue = deque()
            queue.append([x,y])
            while queue:
                x, y = queue.popleft()
                s[x][y] = 0
                for k in range(4):
                    _i, _j = x+dx[k], y+dy[k]
                    if 0<=_i<m and 0<=_j<n and s[_i][_j]==1:
                        queue.append([_i, _j])
                        
    for i in range(t):
        m, n, k = map(int, input().split())
        s = [[0] * n for _ in range(m)]
        cnt = 0
        
        for j in range(k):
            a, b = map(int, input().split())
            s[a][b] = 1
        

        for q in range(m):
            for w in range(n):
                if s[q][w]==1:
                    bfs(s, q, w)
                    cnt += 1
                    
        print(cnt)
                    
if __name__=='__main__':
    solution()