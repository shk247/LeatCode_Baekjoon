from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return True
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        check = set()
        for num in nums:
            if num in check:
                return True
            check.add(num)
        return False