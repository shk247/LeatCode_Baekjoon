import sys 

def mysolution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    nums = [i for i in range(1, n+1)]
    ans = []
    idx = -1 
    while nums:
        idx = (idx+k)%len(nums)
        ans.append(nums[idx])
        del nums[idx]
        if idx!=0:
            idx -= 1
    print(ans)    
        
def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    nums = [i for i in range(1, n+1)]
    ans = []
    idx = 0
    for _ in range(n):
        idx = (idx+k-1)%len(nums)
        ans.append(str(nums.pop(idx)))
        
    print('<'+', '.join(ans)+'>')

if __name__=='__main__':
    solution()