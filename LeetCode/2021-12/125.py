class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(list(filter(str.isalnum, s.lower())))
        if len(s)<=1:
            return True
        end = len(s)-1
        for start in range(len(s)//2):
            if s[start] != s[end]:
                return False
            end-=1
        return True
    
    def isPalindrome2(self, s: str) -> bool:
        i, j = 0, len(s)-1
        
        while i<j:
            while i<j and not s[i].isalnum():
                i += 1
            while i<j and not s[j].isnumeric():
                j -= 1
                
            if s[i].islower() != s[j].islower():
                return False

            i += 1
            j-= 1
        
        return True
    

if __name__=='__main__':
    print(Solution().isPalindrome("0P"))