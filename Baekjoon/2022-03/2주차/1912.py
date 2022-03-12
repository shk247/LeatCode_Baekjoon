import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = [0] + list(map(int, input().split()))
    sum = [-1001]*(n+1)
    
    for i in range(1, n+1):
        sum[i] = max(nums[i], sum[i-1]+nums[i])
        
    print(max(sum))
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    sum = [nums[0]]
        
    for i in range(n-1):
        sum.append(max(sum[i]+nums[i+1], nums[i+1]))
    
    print(max(sum))        
    
if __name__=='__main__':
    mysolution()