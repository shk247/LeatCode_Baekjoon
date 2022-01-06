import sys 

def mysolution():
    input = sys.stdin.readline
    k = int(input())
    
    
def solution():
    input = sys.stdin.readline
    k = int(input())
    nodes = list(map(int, input().split()))
    ans = [[] for _ in range(k)]
    
    def check(arr, depth):
        mid = len(arr)//2
        ans[depth].append(arr[mid])
        if len(arr)==1:
            return
        check(arr[:mid], depth+1)
        check(arr[mid+1:], depth+1)
        
    check(nodes, 0)
    for a in ans:
        print(*a)

if __name__=='__main__':
    solution()