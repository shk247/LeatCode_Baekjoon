from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, t1, t2):
        if t1==None and t2==None:
            return True
        if t1==None or t2==None:
            return False
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
    
    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        q = []
        q.append(root)
        q.append(root)
        
        while q:
            t1 = q.pop()
            t2 = q.pop()
            
            if t1==None and t2==None:
                continue
            if (t1==None or t2==None) or (t1.val != t2.val):
                return False
            
            q.append(t1.left)
            q.append(t2.right)

            q.append(t1.right)
            q.append(t2.left)
        
        return True
    
if __name__=='__main__':
    Solution()