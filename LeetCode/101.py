from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def check(self, left, right):
        if left == None and right == None:
            return True
        if left == None or right == None:
            return False
        if left.val != right.val:
            return False
        return self.check(left.right, right.left) and self.check(left.left, right.right)
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root, root)
    
    def isSymmetric1(self, root: Optional[TreeNode]) -> bool:
        left = root
        right = root
        while True:
            if left == None and right == None:
                break
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            left = left.left
            right = right.right
            
        left = root
        right = root
        while True:
            if left == None and right == None:
                break
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            left = left.right
            right = right.left
        
        return True
    
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        queue = []
        queue.append(root)
        queue.append(root)
        
        while queue:
            t1 = queue.pop()
            t2 = queue.pop()
            if t1 == None and t2 == None:
                return True
            if t1 == None or t2 == None:
                return False
            if t1.val != t2.val:
                return False
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)
        return True
            
             
    
            