import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = []
    
    def back(arr):
        if len(arr) == m:
            print(' '.join(arr))
            return
        
        for i in range(1, n+1):
            if i not in arr:
                arr.append(i)
                back(arr)
                arr.pop()
                
    back(arr)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()