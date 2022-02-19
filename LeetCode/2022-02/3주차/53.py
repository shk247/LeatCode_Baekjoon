from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        answer = -1e9
        for i in range(size):
            tmp = 0 
            for j in range(i, size):
                tmp += nums[j]
                answer = max(answer, tmp)
        return answer
    
    def maxSubArray2(self, nums: List[int]) -> int:
        n = [0 for i in range(len(nums))]
        n[0] = nums[0]
        for i in range(1, len(nums)):
            n[i] = max(n[i-1] + nums[i], nums[i])
        return max(n)
    
    def maxSubArray3(self, nums: List[int]) -> int:
        tmp = answer = nums[0]
        
        for num in nums[1:]:
            tmp = max(num, tmp+num)
            answer = max(answer, tmp)
            
        return answer
    
if __name__=='__main__':
    Solution().maxSubArray([])