
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = 0 
    
        def check(root):
            nonlocal answer
            if root.left is None and root.right is None:
                return root.val 

            left = self.maxPathSum(root.left)
            right = self.maxPathSum(root.right)
            total = root.val + left + right 
            
            answer = max(left, right, total)
            
            return total 
        
        check(root)
        
        return answer
    
    def maxPathSum2(self, root: Optional[TreeNode]) -> int:
        
        def gain(node):
            nonlocal answer 
            
            if not node:
                return 0 
            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)
            
            answer = max(answer, left_gain + right_gain + node.val)
            
            return node.val + max(left_gain, right_gain)

        answer = -1e9
        gain(root)
        
        return answer
        