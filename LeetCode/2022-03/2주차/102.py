from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:
            return answer 
        
        def helper(node, level):
            if len(answer)==level:
                answer.append([])
            
            answer[level].append(node.val)
            
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
            
        helper(root, 0)
        return answer
    
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:
            return answer
        
        q = deque([root])
        
        while q:
            answer.append([])
            level_length = len(q)
            
            for _ in range(level_length):
                node = q.popleft()
                answer[-1].append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return answer        