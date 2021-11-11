from typing import List

class MySolution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0 
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                diff = prices[j]-prices[i]
                if max<diff:
                    max = diff
        return max
    
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice = 0
        minprice = 1e9
        for price in prices:
            if price < minprice:
                minprice = price
            elif price-minprice > maxprice:
                maxprice = price-minprice
        return maxprice
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))