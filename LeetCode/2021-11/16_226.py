from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class MySolution:
    def __init__(self):
        self.answer = []
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root.val is None:
            return
        
        if root.left and root.right:
            if root.left.val < root.right.val:
                self.answer.append(root.right.val)
                self.answer.append(root.left.val)
            else:
                self.answer.append(root.left.val)
                self.answer.append(root.right.val)
            
            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return self.answer
    
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        right = self.invertTree(root.right)
        left = self.invertTree(root.left)
        root.left = right
        root.right = left
        return root
    
    def invertTree2(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        queue = deque()
        queue.append(root)
        
        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left
            queue.append(current.left)
            queue.append(current.right)
        
        return root 
        
        
if __name__=='__main__':
    node = TreeNode(4)
    node.left = TreeNode(2)
    node.left.left = TreeNode(1)
    node.left.right = TreeNode(3)
    node.right = TreeNode(7)
    node.right.left = TreeNode(6)
    node.right.right = TreeNode(9)
    
    sol = Solution()
    print(sol.invertTree(node))