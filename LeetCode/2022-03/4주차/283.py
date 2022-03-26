from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        idx = cnt = 0 
        while cnt!=len(nums):
            cnt+=1
            if nums[idx]==0:
                del nums[idx]
                nums.append(0)
            else:
                idx+=1
            
if __name__=='__main__':
    Solution().moveZeroes([0,0,1])