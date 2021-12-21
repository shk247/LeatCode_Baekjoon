from typing import List
from typing_extensions import Required

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0 
        for i in range(len(height)):
            for j in range(1+i, len(height)):
                area = max(area, min(height[i], height[j])*(j-i))
        return area
    def maxArea2(self, height: List[int]) -> int:
        area = 0 
        left = 0
        right = len(height)-1
        
        while left<right:
            area = max(area, min(height[left], height[right])*(right-left))
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        
        return area
        
if __name__=='__main__':
    print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))