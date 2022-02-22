import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = list(map(int, input().split()))
    nums_size = len(nums)
    plus, minus, multiple, divide = map(int, input().split())
    max_answer = -1e9
    min_answer = 1e9
    
    def dfs(total, idx, plus, minus, multiple, divide):
        nonlocal max_answer, min_answer, nums_size
        if idx==nums_size:
            max_answer = max(max_answer, total)
            min_answer = min(min_answer, total)
            return
        
        if plus:
            dfs(total+nums[idx], idx+1, plus-1, minus, multiple, divide)
        if minus:
            dfs(total-nums[idx], idx+1, plus, minus-1, multiple, divide)
        if multiple:
            dfs(total*nums[idx], idx+1, plus, minus, multiple-1, divide)
        if divide:
            if total<0:
                dfs(((total*-1)//nums[idx])*-1, idx+1, plus, minus, multiple, divide-1)
            else:
                dfs(total//nums[idx], idx+1, plus, minus, multiple, divide-1)
            
    dfs(nums[0], 1, plus, minus, multiple, divide)
    print(max_answer, min_answer)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()