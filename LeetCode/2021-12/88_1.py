from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(m, len(nums1)):
            nums1[i] = nums2[i-m]
        
        nums1.sort()
        
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m-1, n-1
        
        for p in range(n+m-1, -1, -1):
            if p2<0:
                break
            if p1>=0 and nums1[p1]>nums2[p2]:
                nums1[p] = nums1[p1]
                p1-=1
            else:
                nums1[p] = nums2[p2]
                p2-=1
        
        
if __name__=='__main__':
    print(Solution().merge([1]))