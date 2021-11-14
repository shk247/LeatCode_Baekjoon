class MySolution:
    def searchInsert(self, nums, target) -> int:
        mid = len(nums)//2
        while mid != 0 and mid != len(nums):
            if nums[mid]>target:
                mid //= 2
            elif nums[mid]<target:
                mid += (mid//2)
            else:
                return mid
        else:
            return mid
        
class Solution:
    def searchInsert(self, nums, target) -> int:
        left = 0 
        right = len(nums)-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
            else:
                return mid
            
        return left
            
if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1,3],2))
            
            
        