from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        answer = 0 
        
        def search(node):
            nonlocal answer
            if not node:
                return 0 
            
            left_sum = max(0, search(node.left))
            right_sum = max(0, search(node.right))

            answer = max(answer, node.val+left_sum+right_sum)
            return node.val + max(left_sum, right_sum)
        
        search(root)

        return answer
        
        
if __name__=='__main__':
    node = TreeNode(-10)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    
    Solution().maxPathSum(node)
    