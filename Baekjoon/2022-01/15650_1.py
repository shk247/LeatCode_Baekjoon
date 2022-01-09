import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int,input().split())
    
    def back(arr):
        if len(arr)==m:
            print(' '.join(map(str, arr)))
            return
        
        for i in range(1, n+1):
            if not arr or (len(arr)>0 and arr[-1]<i):
                arr.append(i)
                back(arr)
                arr.pop()
                
    back([])
    
def solution():
    input = sys.stdin.readline
    n, m = map(int,input().split())
    s = []
    def dfs(start):
        if len(s)==m:
            print(' '.join(map(str, s)))
            return
        for i in range(start, n+1):
            s.append(i)
            dfs(i+1)
            s.pop()
            
    dfs(1)

if __name__=='__main__':
    mysolution()