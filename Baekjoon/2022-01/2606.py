import sys 
from collections import defaultdict, deque

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    dict = defaultdict(list)
    visited = [False]*(n+1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
    
    def dfs(node):
        visited[node] = True
        print('node=',node,'dict[node]=',dict[node])
        for n in dict[node]:
            if visited[n] == False:
                dfs(n)  
                
    dfs(1)
    print(dict)
    print(visited.count(True)-1)
                
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    dict = defaultdict(list)
    visited = [False]*(n+1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
    
    queue = deque()
    queue.append(1)
    
    while queue:
        v = queue.pop()
        visited[v] = True
        for d in dict[v]:
            if visited[d] == False:
                queue.append(d)
                
    print(visited.count(True)-1)
    

if __name__=='__main__':
    solution()