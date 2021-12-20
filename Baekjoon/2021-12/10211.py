import sys 

def mysolution():
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        ans = -1e9
        for i in range(len(nums)):
            tmp = 0
            for j in range(i, len(nums)):
                tmp += nums[j]
            ans = max(ans, tmp)
        
        print(ans)
    
def solution():
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().split()))
        
        for i in range(1, n):
            if nums[i-1]>0:
                nums[i] += nums[i-1]
                
        print(max(nums))

if __name__=='__main__':
    solution()