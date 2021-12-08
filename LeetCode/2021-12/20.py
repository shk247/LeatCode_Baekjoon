from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        s = deque(s)
        check = []
        while s:
            c = s.popleft()
            if c == '(' or c =='{' or c =='[':
                check.append(c)
            else:
                if not check:
                    return False
                if c == ')' and check[-1] != '(':
                    return False
                elif c == ']' and check[-1] != '[':
                    return False
                elif c == '}' and check[-1] != '{':
                    return False
                check.pop()
        if check:
            return False
        else:
            return True
    
    def isValid2(self, s: str) -> bool:
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        for char in s:
            if char in mapping:
                if not stack or mapping[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return not stack 
        

if __name__=='__main__':
    print(Solution().isValid("()"))