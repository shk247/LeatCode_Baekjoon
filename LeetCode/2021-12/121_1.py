from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 1e9
        answer = 0 
        
        for price in prices:
            if price<min_price:
                min_price = price
            if price-min_price>answer:
                answer = price-min_price
        
        return answer
    
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0 
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                tmp = prices[j] - prices[i]
                answer = max(answer, tmp)
        return answer
                

if __name__=='__main__':
    Solution().maxProfit([7,1,5,3,6,4])