from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = -1e9
        for i in range(len(prices)):
            start = prices[i]
            for j in range(i+1, len(prices)):
                maximum = max(maximum, prices[j]-start)
                
        if maximum<0:
            return 0 
        else:
            return maximum
    
    def maxProfit2(self, prices: List[int]) -> int:
        maximum = -1e9
        left, right = 0, len(prices)-1
        
        if len(prices)==2:
            maximum = prices[right]-prices[left]
        else:
            while left<right:
                maximum = max(prices[right]-prices[left], maximum)
                if prices[left]>prices[right]:
                    left += 1
                else:
                    right -= 1
            
        return maximum 
    
    def maxProfit3(self, prices: List[int]) -> int:
        minprice = 1e9
        maximum = 0
        
        for i in range(len(prices)):
            minprice  = min(minprice, prices[i])
            maximum = max(maximum, prices[i]-minprice)
            
        return maximum
        

if __name__=='__main__':
    print(Solution().maxProfit2([1, 2, 4]))