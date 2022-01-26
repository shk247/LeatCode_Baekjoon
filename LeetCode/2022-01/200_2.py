from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0 
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]
        
        def dfs(i, j):
            grid[i][j] = '0'
            for k in range(4):
                _i = i+dx[k]
                _j = j+dy[k]
                if 0<=_i<len(grid) and 0<=_j<len(grid[0]) and grid[_i][_j]=='1':
                    dfs(_i, _j)
                    
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
                    
        return cnt
    
    def numIslands2(self, grid: List[List[str]]) -> int:
        cnt = 0 
        dx = [0, 0, 1, -1]
        dy = [-1, 1, 0, 0]
        
        row = len(grid)
        col = len(grid[0])
        q = deque()
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    cnt += 1
                    grid[i][j] = '0'
                    q.append([i,j])
                    while q:
                        a, b = q.popleft()
                        for k in range(4):
                            _i = a+dx[k]
                            _j = b+dy[k]
                            if 0<=_i<row and 0<=_j<col and grid[_i][_j]=='1':
                                grid[_i][_j] = '0'
                                q.append([_i,_j])
                                
        return cnt

if __name__=='__main__':
    print(Solution().numIslands2([["1","0","1","1","1"],["1","0","1","0","1"],["1","1","1","0","1"]]))