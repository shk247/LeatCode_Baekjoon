class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        x = str(x)
        mid = len(x)//2
        forward = x[:mid]
        if len(x)%2==1:
            mid += 1 
        backward = x[mid:]
        if forward==backward[::-1]:
            return True
        else:
            return False
        
    def isPalindrome2(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):
            return False
        reversnum = 0 
        while x>reversnum:
            reversnum = reversnum*10 + x%10
            x /= 10
        if x==reversnum or x == reversnum/10:
            return True
        else:
            return False
        
    def isPalindrome3(self, x: int) -> bool:
        if x<0:
            return False
        x = str(x)
        for i in range(len(x)//2):
            if x[i] != x[-i-1]:
                return False
        return True
        
if __name__=='__main__':
    print(Solution().isPalindrome2(12321))