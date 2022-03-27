from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j]==target:
                    return [i, j]
                
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i] 
            hashmap[target-nums[i]] = i 
                