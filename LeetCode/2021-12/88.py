from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
            
        nums1.sort()
    
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1_copy = nums1[:m]
        p1, p2 = 0, 0
        for p in range(m+n):
            if p2>=n or (p1<m and nums1_copy[p1]<=nums2[p2]):
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p1]
                p2 += 1
                
    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m-1, n-1
        
        for p in range(n+m-1, -1, -1):
            if p2<0:
                break
            if p1>=0 and nums1[p1]>nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
                
            
        
        
if __name__=='__main__':
    Solution().merge([1,2,3,0,0,0], 3, [2,5,6], 3)