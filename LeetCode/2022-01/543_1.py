from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0 
        
        def check(node):
            if not node:
                return 0 
            
            left = check(node.left)
            right = check(node.right)
            
            nonlocal answer
            answer = max(answer, left+right)
            
            return max(left, right)+1
        
        check(root)
        
        return answer