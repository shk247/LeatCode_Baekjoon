from typing import List 
from collections import Counter

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        l = set()
        for num in nums:
            if num not in l:
                l.add(num)
            else:
                return num 
            
    def findDuplicate2(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]
            
    def findDuplicate3(self, nums: List[int]) -> int:
        
        cnt = Counter(nums)
        
        for key, value in cnt.items():
            if value != 1:
                return key

if __name__=='__main__':
    Solution()