
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        row = len(grid)
        col = len(grid[0])
        
        def dfs(i, j):
            grid[i][j] = '0'
            for k in range(4):
                nx, ny = i+dx[k], j+dy[k]
                if 0<=nx<row and 0<=ny<col and grid[nx][ny]=='1':
                    dfs(nx, ny)
        answer = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i, j)
                    answer += 1
        return answer
    
    def numIslands2(self, grid: List[List[str]]) -> int:
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        row = len(grid)
        col = len(grid[0])
        
        answer = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    grid[i][j]='0'   
                    q = deque()
                    q.append([i, j])
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            nx, ny = x+dx[k], y+dy[k]
                            if 0<=nx<row and 0<=ny<col and grid[nx][ny]=='1':
                                q.append([nx, ny])
                                grid[nx][ny]='0'
                    answer += 1
                    
        return answer 
        