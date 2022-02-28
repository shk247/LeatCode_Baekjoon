from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0 
        right = len(height)-1
        answer = 0 
        
        while left<right:
            length = min(height[left], height[right])
            width = right-left
            answer = max(answer, length*width)
            
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
                
        return answer
    
    
if __name__=='__main__':
    print(Solution().maxArea([1,1]))