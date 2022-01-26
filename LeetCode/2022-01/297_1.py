from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize_bfs(self, root):
        if not root:
            return ''
        
        answer = []
        q = deque()
        q.append(root)
        
        while q:
            node = q.popleft()
            if not node:
                answer.append('null')
            else:
                answer.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
                
        return ' '.join(answer)
        

    def deserialize_bfs(self, data):
        if not data:
            return None
        nodes = list(data.split())
        root = TreeNode(nodes[0])
        q = deque()
        q.append(root)
        
        for i in range(1, len(nodes), 2):
            if not q:
                break 
            node = q.popleft()
            if nodes[i] != 'null':
                node.left = TreeNode(int(nodes[i]))
                q.append(node.left)
            if nodes[i+1] != 'null':
                node.right = TreeNode(int(nodes[i+1]))
                q.append(node.right)
        return root 
    
    
    def serialize_dfs(self, root):
        if not root:
            return ''
        
        strs = ''
        
        def dfs(node):
            nonlocal strs 
            if not node:
                strs += ' null '
            else:
                strs += (' ' + str(node.val))
                dfs(node.left)
                dfs(node.right)
                    
        dfs(root)
        
        return strs
            
        
    def deserialize_dfs(self, data):
        nodes = deque(data.split())
        
        def dfs(l):
            if not l:
                return 
            
            if l[0] == 'null':
                l.popleft()
                return None
            
            root = TreeNode(l[0])
            l.popletf()
            
            root.left = dfs(l)
            root.right = dfs(l)
            
            return root 
        
        return dfs(nodes)
    
    
if __name__ == '__main__':
    Codec().deserialize_dfs("1 2 3 null null 4 5")