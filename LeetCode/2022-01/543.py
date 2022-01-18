from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global ans 
        ans = 0 
        
        def dfs(node):
            global ans
            if not node:
                return 0 
            left = dfs(node.left)
            right = dfs(node.right)
            ans = max(ans, left+right)
            return max(left, right)+1
        
        dfs(root)
        
        return ans
    
    def mysolution(self, root: Optional[TreeNode]) -> int:
        def dfs(node, depth):
            left = right = 0
            if not node.left and not node.right:
                return depth
            if node.left:
                left = dfs(node.left, depth+1)
            if node.right:
                right = dfs(node.right, depth+1)
            return max(left, right)
        
        res = 0 
        
        if root.left:
            res += dfs(root.left, 1)
        if root.right:
            res += dfs(root.right, 1)
                    
        return res
    
    
if __name__=='__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    # node.right = TreeNode(3)
    # node.left.left = TreeNode(4)
    # node.left.right = TreeNode(5)
    
    print(Solution().diameterOfBinaryTree(node))