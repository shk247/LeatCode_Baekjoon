import sys 
from collections import defaultdict, deque
import heapq

def mysolution():
    input = sys.stdin.readline
    # 도시 개수, 도로 개수, 거리 정보, 출발 도시 번호 
    n, m, k, x = map(int, input().split())
    dict = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        dict[a].append([b,1])
    
    stack = [*dict[x]]
    dp = [1e9]*(n+1)

    while stack:
        road, value = stack.pop()
        if dp[road]>value:
            dp[road] = value
            for r, v in dict[road]:
                if dp[r] > v + value:
                    dp[r] = v + value
                    stack.append([r, v + value])
        
    if k in dp:
        for i in range(len(dp)):
            if dp[i]==k:
                print(i)
    else:
        print(-1)
                

def solution_bfs():
    input = sys.stdin.readline
    n, m, k, x = map(int, input().split())
    graph = defaultdict(list)
    distance = [0] * (n+1)
    visited = [False] * (n+1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        
    def bfs(start):
        q = deque([start])
        visited[start] = True
        distance[start] = 0 
        
        while q:
            now = q.popleft()
            for i in graph[now]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
                    distance[i] = distance[now] + 1 
                    
        if k in distance:
            for i in range(n+1):
                if distance[i]==k:
                    print(i)
        else:
            print(-1)
            
    bfs(x)
    
def solution_dij():
    f = sys.stdin.readline
    INF = int(1e9)

    n, m, k, x = map(int, f().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(m):
        a, b = map(int, f().split())
        graph[a].append((b, 1))

    def dijkstra(start):
        q = []
        q.append((0, start))
        distance[start] = 0
        while q:
            dist, now = q.pop()
            if distance[now] < dist: continue
            for j in graph[now]:
                cost = dist + j[1]
                if cost < distance[j[0]]:
                    distance[j[0]] = cost
                    q.append((cost, j[0]))
    dijkstra(x)
    answer = []
    for i in range(1, n+1):
        if distance[i] == k: answer.append(i)

    if len(answer) == 0: print(-1)
    else:
        for i in answer: print(i, end='\n')

if __name__=='__main__':
    solution_dij()