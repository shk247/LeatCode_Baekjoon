import sys 

def mysolution():
    input = sys.stdin.readline
    k = int(input())
    visited = list(map(int, input().split()))
    left, top, right = [], [], []
    
def solution():
    input = sys.stdin.readline
    k = int(input())
    visited = list(map(int, input().split()))
    answer = [[] for _ in range(k)]
    
    def tree(arr, depth):
        mid = len(arr)//2
        answer[depth].append(arr[mid])
        if len(arr)==1:
            return
        tree(arr[:mid], depth+1)
        tree(arr[mid+1:], depth+1)
    
    tree(visited, 0)
    
    for i in answer:
        print(*i)

if __name__=='__main__':
    solution()