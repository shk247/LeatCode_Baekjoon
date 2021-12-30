import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    num_sum = [0]
    for i in range(len(nums)):
        num_sum.append(num_sum[-1]+nums[i])
        
    for _ in range(m):
        a, b = map(int, input().split())
        print(num_sum[b]-num_sum[a-1])
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()