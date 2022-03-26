from typing import List

class Solution:
    
    def singleNumber(self, nums: List[int]) -> int:
        l = set()
        for num in nums:
            if num in l:
                l.remove(num)
            else:
                l.add(num)
        
        return list(l)[0]