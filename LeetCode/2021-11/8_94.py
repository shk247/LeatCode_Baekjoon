from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 

class Solution:
    def __init__(self):
        self.traversal = []
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return [] 
        
        self.inorderTraversal(root.left)
        self.traversal.append(root.val)
        self.inorderTraversal(root.right)

        return self.traversal
    
    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        answer = []
        current_node = root

        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            answer.append(current_node.val)
            current_node = current_node.right
        return answer

if __name__=="__main__":
    solution = Solution()
    r = TreeNode(1)
    r.right = TreeNode(2)
    r.right.left = TreeNode(3)
    print(solution.inorderTraversal2(r))