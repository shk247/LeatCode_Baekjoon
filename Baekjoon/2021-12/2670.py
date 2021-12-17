import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(float(input()))
    max_val = 1
    for i in range(len(nums)):
        tmp = 1
        for j in range(i, len(nums)):
            tmp *= nums[j]
            max_val = max(max_val, tmp)
    print(round(max_val, 4))
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    li = [float(input()) for _ in range(n)]
    for i in range(1, n):
        li[i] = max(li[i], li[i]*li[i-1])
    print(li)
    

if __name__=='__main__':
    solution()