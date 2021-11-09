from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class MySolution:
    def __init__(self) -> None:
        self.depth = 0 
    def depth_check(self, depth, root):
        if root:
            depth += 1
            left = self.depth_check(depth, root.left)
            right = self.depth_check(depth, root.right)
        return max(left, right)
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.depth_check(0, root)
    
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            return max(left, right) +1  
    
    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        stack = []
        if root is not None:
            stack.append((1, root))
        depth = 0 
        while stack:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth+1, node.left))
                stack.append((current_depth+1, node.right))
        return depth
        
        
if __name__ == '__main__':
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    
    sol = Solution()
    print(sol.maxDepth(node))