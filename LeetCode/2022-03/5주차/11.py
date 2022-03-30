from typing import List

class Solution:
    def maxArea(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums)-1
        answer = 0 
        
        while left<right:
            answer = max(answer, min(nums[left], nums[right])*(right-left))
            if nums[left]<nums[right]:
                left+=1
            else:
                right-=1
        print(answer)
        return answer

if __name__=='__main__':
    Solution().maxArea([1,1])