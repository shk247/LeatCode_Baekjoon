from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = defaultdict(int)
        for num in nums:
            dict[num] += 1
            if dict[num]>1:
                return True
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        table = set()
        for num in nums:
            if num in table:
                return True
            table.add(num)
        return False

        
if __name__=='__main__':
    Solution().containsDuplicate2([1,2,3,1])