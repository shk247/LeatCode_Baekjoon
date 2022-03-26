from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        min_price = prices[0] 
        answer = 0 
        
        for price in prices:
            min_price = min(min_price, price)
            if price>min_price:
                answer = max(answer, price-min_price)
            
        return answer
            