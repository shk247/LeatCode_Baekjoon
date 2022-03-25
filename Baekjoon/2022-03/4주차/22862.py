import sys

def mysolution():
    input = sys.stdin.readline
    
def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    end = 0 
    arr_cnt = 0 
    odd_cnt = 0
    answer = 0 
    flag = 1
    
    for start in range(len(arr)):
        while odd_cnt<=k and flag:
            if arr[end]%2:
                if odd_cnt==k:
                    break
                odd_cnt+=1
            
            if end == n-1:
                flag = False
                break
            
            arr_cnt+=1
            end+=1
        
        answer = max(answer, arr_cnt-odd_cnt)
        
        if arr[start]%2:
            odd_cnt-=1
        
        arr_cnt-=1
        
    print(answer)

if __name__=='__main__':
    mysolution()