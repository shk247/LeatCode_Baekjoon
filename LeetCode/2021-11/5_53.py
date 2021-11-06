from typing import List
import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sub = max_sub = nums[0]

        for num in nums[1:]:
            current_sub = max(num, current_sub+num)
            max_sub = max(current_sub, max_sub)
        
        return max_sub

    def maxSubArray2(self, nums: List[int]) -> int:
        return self.findBestSubarray(nums, 0, len(nums)-1)

    def findBestSubarray(self, nums, left, right):
        if left>right:
            return -math.inf

        mid = (left+right)//2
        curr = best_left_sum = best_right_sum = 0

        for i in range(mid-1, left-1, -1):
            curr += nums[i]
            best_left_sum = max(best_left_sum, curr)

        curr = 0
        for i in range(mid+1, right+1):
            curr += nums[i]
            best_right_sum = max(best_right_sum, curr)

        best_combined_sum = nums[mid] + best_left_sum + best_right_sum

        left_half = self.findBestSubarray(nums, left, mid-1)
        right_half = self.findBestSubarray(nums, mid+1, right)

        return max(best_combined_sum, left_half, right_half)
        


if __name__ == '__main__':
    Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])