from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
    
    def containsDuplicate2(self, nums: List[int]) -> bool:
        dict = {}
        
        for num in nums:
            if dict.get(num):
                return True
            dict[num]=1
        return False
    
if __name__=='__main__':
    print(Solution().containsDuplicate2([1,1,1,3,3,4,3,2,4,2]))