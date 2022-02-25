from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0
        max_num = prices[0]
        min_num = prices[0]
        for price in prices[1:]:
            if min_num>price:
                max_num = price
                min_num = price
            elif max_num<price:
                max_num=price
                answer=max(answer, max_num-min_num)
            
        return answer
    
    def maxProfit2(self, prices: List[int]) -> int:
        min_price = 1e9
        answer = 0 
        
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i]-min_price > answer:
                answer = prices[i]-min_price        
            
        return answer            