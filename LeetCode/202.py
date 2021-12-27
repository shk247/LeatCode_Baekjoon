class Solution:
    def isHappy(self, n: int) -> bool:
        tmp = []
        while True:
            n = list(str(n))
            total = 0 
            for i in range(len(n)):
                total += int(n[i])**2
            if total == 1:
                return True
            if total in tmp:
                return False
            n = total 
            tmp.append(n)
    
    def isHappy2(self, n: int) -> bool:
        def get_next(n):
            total = 0 
            while n>0:
                n, digit = divmod(n, 10)
                total += digit**2
            return total
            
        seen = set()
        while n!=1 and n not in seen:
            seen.add(n)
            n = get_next(n)
            
        return n==1
    
    def isHappy2(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum
        
        slow = n
        fast = get_next(n)
        
        while fast != 1 and fast != slow:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            
        return fast == 1


if __name__=='__main__':
    print( Solution().isHappy(3))