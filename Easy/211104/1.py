from itertools import combinations

def mysolution(nums, target):
    com = combinations(nums, 2)
    answer = [[a, b] for a,b in list(com) if a+b==target]
    return [i for i,v in enumerate(nums) if v==answer[0][0] or v==answer[0][1]]

# brute-force : O(n^2)
def solution(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

# hashmap 
def solution2(nums, target):
    hashmap = {}
    for i,v in enumerate(nums):
        diff = target - v
        if diff in hashmap:
            return [i, hashmap[diff]]
        hashmap[v] = i

if __name__ == '__main__':
    print(solution2([2,7,11,15], 9))