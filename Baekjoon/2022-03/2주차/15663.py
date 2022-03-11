import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    answer = []

    def backtraking(arr, size):
        nonlocal answer
        if size==m:
            answer.append(arr)
            return
        for num in nums:
            if num not in arr:
                arr.append(num)
                backtraking(arr, size+1)
                arr.pop()
                
    backtraking([], 0)
    print(answer)
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = sorted(list(map(int, input().split())))
    visited = [False] * n
    temp = []
    
    def dfs():
        if len(temp)==m:
            print(*temp)
            return
        
        pre = -1 
        for i in range(n):
            if not visited[i] and pre!=nums[i]:
                pre = nums[i]
                visited[i]=True
                temp.append(nums[i])
                dfs()
                visited[i]=False
                temp.pop()
        
    dfs()
    
    def solution2():
        input = sys.stdin.readline
        n, m = map(int, input().split())
        nums = sorted(list(map(int, input().split())))
        dict = {}
        visited = [0]*(n)
        temp = []
        
        def dfs():
            if len(temp)==m:
                s = ' '.join(map(str, temp))
                if s not in dict:
                    dict[s]=1
                    print(s)
                return
            
            for i in range(n):
                if not visited[i]:
                    visited[i]=True
                    temp.append(nums[i])
                    dfs()
                    visited[i]=False
                    temp.pop()
        
        dfs()                    

if __name__=='__main__':
    solution()