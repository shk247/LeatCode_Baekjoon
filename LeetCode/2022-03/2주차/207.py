from collections import defaultdict, deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        dict = defaultdict(list)
        
        for pre in prerequisites:
            a, b = pre
            indegree[a]+=1
            dict[b].append(a)
            
        q = deque()
        for i in range(numCourses):
            if indegree[i]==0:
                q.append(i)
                
        if not q:
            return False
        
        while q:
            a = q.popleft()
            for d in dict[a]:
                indegree[d]-=1
                if indegree[d]==0:
                    q.append(d)
              
        for i in range(numCourses):
            if indegree[i]!=0:
                return False
            
        return True
    
    
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dict = defaultdict(list)
        
        for relation in prerequisites:
            next, pre = relation[0], relation[1]
            dict[pre].append(next)
            
        checked = [False]*numCourses
        path = [False]*numCourses
        
        for curr in range(numCourses):
            if self.isCyclic(curr, dict, checked, path):
                return False
        
        return True
    
    def isCyclic(self, curr, dict, checked, path):
        if checked[curr]:
            return False
        
        if path[curr]:
            return True
        
        path[curr] = True
        
        ret = False
        for child in dict[curr]:
            ret = self.isCyclic(child, dict, checked, path)
            if ret:
                break
            
        path[curr] = False
        checked[curr] = True
        
        return ret
        
if __name__=='__main__':
    Solution()