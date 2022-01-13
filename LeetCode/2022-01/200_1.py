from typing import List
from collections import deque

class Solution:
    def numIslands_dfs(self, grid: List[List[str]]) -> int:
        ans = 0 
        row = len(grid)
        col = len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        def check(i, j):
            grid[i][j] = '0'
            for k in range(4):
                _i, _j = i+dx[k], j+dy[k]
                if 0<=_i<row and 0<=_j<col:
                    if grid[_i][_j] == '1':
                        check(_i, _j)
                
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    check(i, j)
                    ans += 1
        return ans 
    
    
    def numIslands_bfs(self, grid: List[List[str]]) -> int:
        ans = 0 
        row = len(grid)
        col = len(grid[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        def check(i, j):
            queue = deque()
            queue.append([i, j])
            while queue:
                i, j = queue.popleft()
                grid[i][j] = '0'
                
                for k in range(4):
                    _i, _j = i+dx[k], j+dy[k]
                    if 0<=_i<row and 0<=_j<col:
                        if grid[_i][_j] == '1':
                            queue.append([_i, _j])
                
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    check(i, j)
                    ans += 1
        return ans 
     
    def numIslands_unionfind(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0 
        
        nr = len(grid)
        nc = len(grid[0])
        num_islands = 0 
        
        count = 0 
        parent = []
        rank = []
        
                
if __name__=='__main__':
    print(Solution().numIslands_bfs([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))