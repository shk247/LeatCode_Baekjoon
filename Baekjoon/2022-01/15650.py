import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = []
    
    def back(arr):
        if len(arr)==m:
            print(' '.join(map(str, arr)))
            return
        for i in range(1, n+1):
            if len(arr)==0 or arr[-1]<i:
                arr.append(i)
                back(arr)
                arr.pop()
    back(arr)
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    arr = []
    
    def back(start):
        if len(arr)==m:
            print(' '.join(map(str, arr)))
            return
        for i in range(start, n+1):
            arr.append(i)
            back(i+1)
            arr.pop()  
        
    back(1)

if __name__=='__main__':
    solution()