from re import T
import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dict = defaultdict(list)
    
    
def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(100000)
    
    n, m = map(int, input().split())
    visited = [False] * (n+1)
    
    dict = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
    
    def dfs(node):
        visited[node] = True
        for n in dict[node]:
            if visited[n] == False:
                dfs(n)
        
    ans = 0 
    for node in list(dict):
        if visited[node] == False:
            dfs(node)
            ans += 1 

if __name__=='__main__':
    mysolution()