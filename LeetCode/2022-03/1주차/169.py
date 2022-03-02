from collections import Counter
from typing import List
 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]
    
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        candidate = None 
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num==candidate else -1)
        
        return candidate

if __name__=='__main__':
    print(Solution().majorityElement([-1,100,2,100,100,4,100]))