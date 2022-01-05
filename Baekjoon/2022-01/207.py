from typing import List
from collections import defaultdict 

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for x,y in prerequisites:
            graph[x].append(y)
            
        trace = set()
        visited = set()
        
        def dfs(i):
            if i in trace:
                return False
            if i in visited:
                return True
            
            trace.add(i)
            
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            trace.remove(i)
        
            visited.add(i)
            
            return True

        for x in list(graph):
            if not dfs(x):
                return False
    
        return True
    
if __name__=='__main__':
    Solution().canFinish(2, [[1,0],[0,1]])