import sys 
from itertools import combinations

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    total = list(combinations(nums, 3))
    total = [sum(t) for t in total if sum(t)<=m]
    print(max(total))
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    result = 0 
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if nums[i] + nums[j] + nums[k] > m:
                    continue
                else:
                    result = max(result, nums[i] + nums[j] + nums[k])
    print(result)
    
if __name__=='__main__':
    mysolution()