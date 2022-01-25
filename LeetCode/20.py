from collections import deque

class Solution:
    def isValid(self, strs: str) -> bool:
        tmp = []
        q = deque()
        q.extend(list(strs))
        
        while q:
            c = q.popleft()
            if c==')':
                if len(tmp)==0 or tmp[-1]!='(':
                    return False
                else:
                    tmp.pop()
            elif c=='}':
                if len(tmp)==0 or tmp[-1]!='{':
                    return False
                else:
                    tmp.pop()
            elif c==']':
                if len(tmp)==0 or tmp[-1]!='[':
                    return False
                else:
                    tmp.pop()
            else:
                tmp.append(c)
                
        return len(tmp)==0
    
    def isValid2(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', '}':'{', ']':'['}
        
        for c in s:
            if c in mapping:
                if not stack or stack[-1]!=mapping.get(c):
                    return False
                stack.pop() 
            else:
                stack.append(c)
        
        return not stack

if __name__=='__main__':
    print(Solution().isValid2("()"))