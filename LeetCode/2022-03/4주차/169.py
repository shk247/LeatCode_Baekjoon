from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0 
        answer = 0
        
        for num in nums:
            if cnt==0:
                answer = num
                cnt += 1
            elif num==answer:
                cnt+=1
            else:
                cnt-=1
                
        return answer 
        