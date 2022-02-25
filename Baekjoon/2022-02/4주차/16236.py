import sys 
from collections import defaultdict
import heapq

def mysolution():
    input = sys.stdin.readline
    n, e = map(int, input().split())
    dict = defaultdict(list)
    
    for _ in range(e):
        a, b, c = map(int, input().split())
        dict[a].append([b, c])
        dict[b].append([a, c])
    
    def bfs(i, j):
        dij = [1e9]*(n+1)
        dij[i] = 0
        visited = [False]*(n+1)
        visited[i]=True
        
        q = []
        heapq.heappush(q, [0, i])
        
        while q:
            cost, des = heapq.heappop(q)
            for node in dict[des]:
                des2, cost2 = node
                if not visited[des2] and dij[des2]>cost+cost2:
                    visited[des2]=True
                    dij[des2]=cost+cost2
                    heapq.heappush(q, [cost+cost2, des2])
                        
        return dij[j]
    
    a, b = map(int, input().split())
    answer = min(bfs(1,a)+bfs(a,b)+bfs(b,n),  bfs(1,b)+bfs(b,a)+bfs(a,n))
    
    if answer>=1e9:
        print(-1)
    else:
        print(answer)
        
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()