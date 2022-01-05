from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if not (0<=x<len(grid[0]) and 0<=y<len(grid) and grid[x][y]=='1'):
                return

            grid[y][x] = '0'
            
            dfs(x-1, y)
            dfs(x+1, y)
            dfs(x, y-1)
            dfs(x, y+1)
            
        cnt = 0 
        
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    dfs(x, y)
                    cnt += 1
                    
        return cnt 
            
    def numIslands2(self, grid: List[List[str]]) -> int:
        def bfs(i, j):
            queue = deque()
            queue.append((i, j))
            while queue:
                i, j = queue.pop()
                grid[i][j] = '0'
                
                if i-1>0 and grid[i-1][j]=='1' and (i-1,j) not in queue:
                    bfs(i-1, j)
                if i+1<len(grid) and grid[i+1][j] == '1' and (i+1, j) not in queue:
                    bfs(i+1, j)
                if j-1>0 and grid[i][j-1] == '1' and (i, j-1) not in queue:
                    bfs(i, j-1)
                if j+1<len(grid[0]) and grid[i][j+1] == '1' and (i, j+1) not in queue:
                    bfs(i, j+1)
                
        cnt = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    cnt += 1
                    bfs(i, j)
        return cnt
