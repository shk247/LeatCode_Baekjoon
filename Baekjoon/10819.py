import sys 
from itertools import permutations

# 순열 - 라이브러리 
def mysolution():
    input = sys.stdin.readline
    n = int(input())
    nums = map(int, input().split())
    nums = list(permutations(nums, n))
    answer = -1e9  
    for num in nums:
        tmp = 0 
        for i in range(len(num)-1):
            tmp += abs(num[i]-num[i+1])
        answer = max(answer, tmp)
    return answer

# 순열 - 라이브러리x
def mysolution2():
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    arr.sort()
    ans = -1e9
    
    def per(arr):
        k = m = -1
        
        # 증가하는 마지막 부분을 가리키는 k
        for i in range(len(arr)-1):
            if arr[i] < arr[i+1]:
                k = i
                
        # 전체 내림차순일 경우, 반환
        if k == -1:
            return [-1]
        
        # index k 이후 부분 중 값이 k보다 크면서 가장 멀리 있는 index m 찾기
        for i in range(k, len(arr)):
            if arr[k] < arr[i]:
                m = i

        arr[k], arr[m] = arr[m], arr[k]
        
        # k index 이후 오름차순 정렬
        list_a = arr[:k+1] + sorted(arr[k+1:])
        return list_a
    
    while True:
        arr = per(arr)
        
        if arr == [-1]:
            break
        
        tmp = 0 
        for i in range(len(arr)-1):
            tmp += abs(arr[i]-arr[i+1])
        ans = max(ans, tmp)
    
    print(ans)
        
        
# 재귀
def solution_recursive():
    sys.setrecursionlimit(100001)
    input = sys.stdin.readline
    n = int(input())
    input_array = list(map(int, input().split()))
    input_array.sort()
    result_array = sorted(input_array, reverse=True)
    result = 0 
    
    def result_solve(array):
        nonlocal result 
        tmp = 0 
        for i in range(len(array)-1):
            tmp += abs(array[i]-array[i+1])
        result = max(result, tmp)
        
    def fun(array):
        nonlocal result
        
        result_solve(array) 

        if array==result_array:
            print(result)
            exit()
        
        for i in range(n-1, 0, -1):
            if array[i-1]<array[i]:
                for j in range(n-1, 0, -1):
                    if array[i-1]<array[j]:
                        array[i-1], array[j] = array[j], array[i-1]
                        array = array[:i] + sorted(array[i:])
                        fun(array)
                        
    fun(input_array)
    
# dfs
def solution_dfs():
    n = int(input())
    nums = list(map(int, input().split()))
    li, res = [], 0
    check = [0]*n
    
    def dfs(depth):
        nonlocal res
        if depth == n:
            res = max(res, sum(abs(li[i]-li[i+1])for i in range(n-1)))
            return
        
        for i in range(n):
            if check[i]:
                continue
            li.append(nums[i])
            check[i] = 1
            dfs(depth+1)
            li.pop()
            check[i]=0
            
    dfs(0)
    print(res)
    
if __name__=='__main__':
    mysolution2()