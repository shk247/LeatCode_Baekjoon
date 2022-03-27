class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {')':'(', ']':'[', '}':'{'}
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack or stack[-1]!=dict[i]:
                    return False
                stack.pop()
        
        return not stack