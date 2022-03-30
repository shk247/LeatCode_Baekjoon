from typing import List
from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        
        nums.sort()
        total = list(combinations(nums, 3))
        answer = set()
        
        for t in total:
            if sum(t)==0 and t not in answer:
                answer.add(t)
                
        return list(answer)    
    
    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        
        for start in range(len(nums)-2):
            if start>0 and nums[start] == nums[start-1]:
                continue
            
            left = start+1
            right = len(nums)-1
            
            while left<right:
                total = nums[start] + nums[left] + nums[right]
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    answer.append([nums[start], nums[left], nums[right]])
                    
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                        
                    left+=1
                    right-=1
        
        return answer
        
        
if __name__=='__main__':
    Solution()