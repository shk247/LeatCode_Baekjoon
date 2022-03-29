from typing import List 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = 0 
        for i in range(len(nums)):
            tmp = 0 
            for j in range(i, len(nums)):
                tmp += nums[j]
                answer = max(answer, tmp)
        return answer
    
    def maxSubArray2(self, nums: List[int]) -> int:
        dp = [0]*(len(nums))
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            
        return max(dp)
    
    def maxSubArray3(self, nums: List[int]) -> int:
        tmp = answer = nums[0] 
        
        for num in nums[1:]:
            tmp = max(tmp+num, num) 
            answer = max(answer, tmp)
        
        return answer

if __name__=='__main__':
    Solution().maxSubArray([1])