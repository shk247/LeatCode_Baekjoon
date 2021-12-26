import sys 
from collections import defaultdict 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    tree = defaultdict(list)
    parent = [-1]*(n+1)
    for _ in range(n):
        a, b = map(int, input().split()) 
        tree[a].append(b)
        tree[b].append(a)
    
    def dfs(n):
        for node in tree[n]:
            if parent[node] == -1:
                parent[node] = n
                dfs(node)
            
    dfs(2)
    
    for i in range(2, n+1):
        print(parent[i])
        
if __name__=='__main__':
    mysolution()