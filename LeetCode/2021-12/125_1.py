from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(filter(str.isalnum, s.lower()))
        
        right = len(s)-1
        
        for i in range(len(s)//2):
            if s[i] != s[right]:
                return False
            right -= 1
        
        return True
                

if __name__=='__main__':
    Solution().maxProfit([7,1,5,3,6,4])