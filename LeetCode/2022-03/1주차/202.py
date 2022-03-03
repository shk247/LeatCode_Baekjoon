class Solution:
    def isHappy(self, n: int) -> bool:
        nums = [n]
        
        while True:
            num = nums[-1]
            tmp = 0 
            while num!=0:
                num, r = divmod(num, 10)
                tmp += r**2
            if tmp == 1:
                return True
            if tmp in nums:
                return False
            else:
                nums.append(tmp)
                
    def isHappy2(self, n: int) -> bool:
        def get_next(num):
            total = 0 
            while num>0:
                num, r = divmod(num, 10)
                total += r**2
            return total 
        
        slow = n 
        fast = get_next(slow)
        
        while fast!=1 and fast!=slow:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            
        return fast==1

if __name__=='__main__':
    print(Solution().isHappy(19))