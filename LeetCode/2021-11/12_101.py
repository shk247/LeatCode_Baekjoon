class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class MySolution:
    def __init__(self) -> None:
        self.left_arr = []
        self.right_arr = []
        
    def isSymmetric(self, root) -> bool:
        if root.left == None and root.right == None:
            return root.val
        if root.left == None or root.right == None:
            return 
        
        self.left_arr.append(self.isSymmetric(root.left))
        self.right_arr.append(self.isSymmetric(root.right))
        
        return self.left_arr == self.right_arr
                
class Solution:
    def isMirror(self, left, right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        return (left.val==right.val) and self.isMirror(left.right, right.left) and self.isMirror(left.left, right.right)
        
    def isSymmetric(self, root) -> bool:
        return self.isMirror(root, root)
    
    def isSymmetric2(self, root) -> bool:
        queue = [root, root]
        
        while queue:
            left = queue.pop()
            right = queue.pop()
            
            if left == right == None:
                continue
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            
            queue.extend([left.left, right.right, left.right, right.left])
        
        return True
        
        
if __name__=='__main__':
    node = TreeNode(1)
    node.left = TreeNode(2)
    node.left.left = TreeNode(3)
    node.left.right = TreeNode(4)
    node.right = TreeNode(2)
    node.right.left = TreeNode(4)
    node.right.right = TreeNode(3)
    
    sol = Solution()
    print(sol.isSymmetric(node))