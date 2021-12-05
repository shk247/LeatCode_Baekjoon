import sys 
from collections import defaultdict, deque

def mysolution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    relation = defaultdict(deque)    
    for _ in range(n):
        a, b = map(int, input().split())
        relation[a].append(b)
        relation[b].append(a)
    
    for i in range(1,n+1):
        now = defaultdict[i]
        check = [0]*(n+1)
        
        while now:
            friend = now.popleft()
            check[friend]=1
            break
 
    
def solution():
    input = sys.stdin.readline
    N, K = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    check = [-1]*(N+1)
    for _ in range(K):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    def bfs(node):
            q = deque()
            q.append(node)
            check[node] = 0 
            while q:
                node = q.popleft()
                for n in graph[node]:
                    if check[n] == -1:
                        q.append(n)
                        check[n] = check[node]+1
    
    for i in range(1,N+1):
        check = [-1]*(N+1)
        bfs(i)
        if max(check)>6 or -1 in check[1:]:
            return "Small World!"
    return "Big World!"
        
if __name__=='__main__':
    mysolution()