from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = -1e9
        for i in range(len(nums)):
            tmp = 0 
            for j in range(i, len(nums)):
                tmp += nums[j]
                maximum = max(maximum, tmp)
        return maximum
    
    def maxSubArray2(self, nums: List[int]) -> int:
        current = maximum = nums[0]
        for i in range(1, len(nums)):
            current = max(current+nums[i],nums[i])
            maximum = max(current, maximum)
        return maximum
    
    
    def maxSubArray(self, nums: List[int]) -> int:
        def findsub(nums, left, right):
            if left>right:
                return -1e9
            
            mid = (left + right) // 2
            curr = maximum_left = maximum_right = 0 
            
            for i in range(mid-1, left-1, -1):
                curr += nums[i]
                maximum_left = max(maximum_left, curr)
                
            curr = 0 
            
            for i in range(mid+1, right+1):
                curr += nums[i]
                maximum_right = max(maximum_right, curr)
            
            maxinum_sum = nums[mid] + maximum_left + maximum_right
            
            left_half = findsub(nums, left, mid-1)
            right_half = findsub(nums, mid+1, right)
            
            return max(maxinum_sum, left_half, right_half)
        
        return findsub(nums, 0, len(nums)-1)
            
        
if __name__=='__main__':
    print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))