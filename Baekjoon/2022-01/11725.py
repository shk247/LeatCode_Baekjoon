import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    dict = defaultdict(list)
    
    for _ in range(n-1):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
    
    for i in range(2, n+1):
        print(dict[i][0])
    
    
def solution():
    sys.setrecursionlimit(10**9)
    
    input = sys.stdin.readline
    n = int(input())
    parents = [0 for _ in range(n+1)]
    dict = defaultdict(list)
    
    for _ in range(n-1):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
        
    def dfs(node):
        for n in dict[node]:
            if parents[n]==0:
                parents[n]=node
                dfs(n)
    
    for i in range(2, n+1):
        print(parents[i])

if __name__=='__main__':
    mysolution()