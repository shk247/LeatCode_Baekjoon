class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        
        tmp = x
        elements = []
        
        while tmp>0:
            tmp, r = divmod(tmp, 10)
            elements.append(r)
        
        return elements==elements[::-1]
