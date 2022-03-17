import sys 
from itertools import permutations

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    answer = 0 
    for _ in range(n):
        num, strike, ball = map(int, input().split())
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(permutations([1,2,3,4,5,6,7,8,9], 3)) 
    for _ in range(n):
        num, strike, ball = map(int, input().split())
        num = list(map(int, str(num)))
        remove_cnt = 0 
        for i in range(len(nums)):
            strike_cnt = ball_cnt = 0
            i -= remove_cnt 
            for j in range(len(num)):
                if num[j] in nums[i]:
                    if j==nums[i].index(num[j]):
                        strike_cnt+=1
                    else:
                        ball_cnt+=1
            if strike != strike_cnt or ball != ball_cnt:
                nums.remove(nums[i])
                remove_cnt +=1 

    print(len(nums))
                    
    
if __name__=='__main__':
    solution()