from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]
        
    def majorityElement2(self, nums: List[int]) -> int:
        cnt = 0 
        candidate = None 
        
        for num in nums:
            if cnt==0:
                candidate = num
            candidate += (1 if num==candidate else -1)
            
        return candidate