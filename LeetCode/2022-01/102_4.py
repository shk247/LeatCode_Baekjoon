from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        q.append(root)
        answer = []
        
        while q:
            size = len(q)
            answer.append([])
            for _ in range(size):
                node = q.popleft()
                answer[-1].append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return answer
    
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        levels = []
        
        def fun(node, level):
            if len(levels)==level:
                levels.append([])
                
            levels[-1].append(node.val)
            
            if node.left:
                fun(node.left, level+1)
            if node.right:
                fun(node.right, level+1)
                
        fun(root, 0)
        
        return levels
        
        

if __name__=='__main__':
    Solution()