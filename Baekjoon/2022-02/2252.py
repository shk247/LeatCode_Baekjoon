import sys 
from collections import defaultdict, deque

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    indegree = [0] * (n+1)
    dict = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, input().split())
        indegree[b] += 1
        dict[a].append(b)
    
    q = deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
            
    while q:
        node = q.popleft()
        for next in dict[node]:
            indegree[next] -= 1
            if indegree[next]==0:
                q.append(next)
        print(node, end=' ')
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()