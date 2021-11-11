from collections import Counter, defaultdict

class MySolution:
    def singleNumber(self, nums) -> int:
        print(Counter(nums).most_common()[-1][0])
        
class Solution:
    def singleNumber(self, nums) -> int:
        hash_table = defaultdict(list)
        for i in nums:
            hash_table[i] += 1
            
        if i in hash_table:
            if hash_table[i] == 1:
                return i         

if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([4,1,2,1,2]))