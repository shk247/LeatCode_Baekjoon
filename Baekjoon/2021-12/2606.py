import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    computers = int(input())
    n = int(input())
    dict = defaultdict(list)
    for _ in range(n):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
    q = dict[1]
    warm = []
    while q:
        computer = q.pop()
        if computer not in warm and computer != 1:
            warm.append(computer)
            q.extend(dict[computer])
    print(len(warm))

def dfs_solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    dict = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
        
    def dfs(start):
        for i in dict[start]:
            if i not in visited:
                visited.append(i)
                dfs(i)
                
    visited = []
    dfs(1)
    print(len(visited)-1)
    
def bfs_solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    dict = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
        
    def bfs(start):
        queue = dict[start]
        while queue:
            for i in dict[queue.pop()]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)   
    visited = []
    bfs(1)
    print(len(visited)-1)
    
    
if __name__=='__main__':
    dfs_solution()