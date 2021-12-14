from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        answer = 0 
        for i in range(days):
            for j in range(i+1, days):
                diff = prices[j]-prices[i]
                if diff>answer:
                    answer = diff
        return answer
    
    def maxProfit2(self, prices: List[int]) -> int:
        min_value = 1e9
        diff = 0 
        
        for price in prices:
            if price<min_value:
                min_value=price
            elif price-min_value>diff:
                diff = price-min_value
        
        return diff
            
if __name__=='__main__':
    print(Solution().maxProfit2(
[2,4,1]))