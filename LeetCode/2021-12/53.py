from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = -1e9
        
        for i in range(len(nums)):
            sub = nums[i]
            for j in range(i+1, len(nums)):
                sub += nums[j]
                answer = max(answer, sub)
                
        return answer

    def maxSubArray2(self, nums: List[int]) -> int:
        current = answer = nums[0]
        
        for num in nums[1:]:
            current = max(num, current+num)
            answer = max(answer, current)
            
        return answer

        
if __name__=='__main__':
    print(Solution().maxSubArray([1]))