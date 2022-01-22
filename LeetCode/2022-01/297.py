from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        if not root:
            return ''
        q = deque([root])
        answer = []
        while q:
            node = q.popleft()
            if not node:
                answer.append('NULL')
            else:
                answer.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
        return ' '.join(answer)

    def deserialize(self, data):
        if data=='':
            return []
        
        data = data.split()
        root = TreeNode(data[0])
        q = deque([root])
        idx = 1 
        
        while q:
            node = q.popleft()
            if data[idx] != 'NULL':
                node.left = TreeNode(int(data[idx]))
                q.append(node.left)
            idx += 1
            
            if data[idx] != 'NULL':
                node.right = TreeNode(int(data[idx]))
                q.append(node.right)
            idx += 1
            
        return root

if __name__=='__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))