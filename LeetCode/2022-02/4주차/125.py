class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new_s = ''.join([i for i in s if i.isalnum()])
        
        for i in range(len(new_s)//2):
            if new_s[i] != new_s[-1-i]:
                return False
        return True
    
    def isPalindrome2(self, s: str) -> bool:
        left, right = 0, len(s)-1
        s = s.lower()
        
        while left<right:
            while left<right and not s[left].isalnum():
                left += 1
            while left<right and not s[right].isalnum():
                right -= 1
            
            if s[left] != s[right]:
                return False
        
            left += 1
            right -= 1
            
        return True   
        
if __name__=='__main__':
    print(Solution().isPalindrome(' '))