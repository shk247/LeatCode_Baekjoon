import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    def back(arr, arr_size):
        nonlocal m, n
        if arr_size==m:
            print(*arr)
            return
        
        for i in range(1, n+1):
            arr.append(i)
            back(arr, arr_size+1)
            arr.pop()
            
    back([], 0)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()