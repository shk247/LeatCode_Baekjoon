class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x = list(str(x))
        
        for i in range(len(x)//2):
            if x[i] != x[-1-i]:
                return False
        return True

if __name__=='__main__':
    print(Solution().isPalindrome(10))