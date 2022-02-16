import sys 

class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')', '[':']', '{':'}'}
        stack = []
        
        for i in list(s):
            if i in '([{':
                stack.append(i)
            elif not stack or i != dict[stack.pop()]:
                return False
       
        return not stack

if __name__=='__main__':
    print(Solution().isValid("("))