from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = defaultdict(int)
        for i in range(len(nums)):
            dict[nums[i]] += 1
        dict = sorted(dict.items(), key=lambda x: x[1], reverse=True )
        return dict[0][0]
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.majorityElement([1,2,2,1,1,2,2]))