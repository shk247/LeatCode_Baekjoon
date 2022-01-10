from collections import defaultdict, deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        ans = defaultdict(list)
        
        def check(node, depth):
            if node is not None:
                ans[depth].append(node.val)
                check(node.left, depth+1)
                check(node.right, depth+1)
            
        check(root, 0)
        
        return list(ans.values())
    
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(node, level):
            if len(levels) == level:
                levels.append([])
            
            levels[level].append(node.val)
            
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
                
        helper(root, 0)
        
        return levels
    
    def levelOrder2(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        queue = deque([root])
        
        while queue:
            levels.append([])
            length = len(queue)
            
            for _ in range(length):
                node = queue.popleft()
                levels[-1].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        return levels

if __name__=='__main__':
    node = TreeNode(3)
    node.left = TreeNode(9)
    node.right = TreeNode(20)
    node.right.left = TreeNode(15)
    node.right.right = TreeNode(7)
    print(Solution().levelOrder2(node))