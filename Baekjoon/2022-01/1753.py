import sys 
from collections import defaultdict, deque
import heapq

def mysolution():
    input = sys.stdin.readline
    # 정점, 간선
    v, e = map(int, input().split())
    start = int(input())
    dict = defaultdict(list)
    
    for _ in range(e):
        a, b, w = map(int, input().split())
        dict[a].append([b, w])
        
    dis = [1e9]*(v+1)
    dis[start] = 0 
    visited = [False]*(v+1)
    
    q = deque()
    q.extend(dict[start])
    visited[start] = True
    
    while q:
        end, cost = q.popleft()
        if dis[end]>cost:
            dis[end] = cost
            if not visited[end]:
                visited[end] = True
                for d in dict[end]:
                    n, c = d[0], d[1]
                    q.append([n, cost+c])
    
    for i in range(1, v+1):
        if dis[i] == 1e9:
            print('INF')
        else:
            print(dis[i])

    
    
def solution():
    input = sys.stdin.readline
    # 정점, 간선
    v, e = map(int, input().split())
    start = int(input())
    dict = defaultdict(list)
    
    for _ in range(e):
        a, b, w = map(int, input().split())
        dict[a].append([b, w])
        
    dis = [1e9]*(v+1)
    dis[start]=0
    
    heap =[]
    heapq.heappush(heap, [0, start])
    
    while heap:
        now_dis, now = heapq.heappop(heap)
        if dis[now] >= now_dis:
            for i in dict[now]:
                cost = now_dis+i[1]
                if dis[i[0]]>cost:
                    dis[i[0]]=cost
                    heapq.heappush(heap, [cost, i[0]])
                
    for i in range(1, v+1):
        if dis[i] == 1e9:
            print('INF')
        else:
            print(dis[i])
    
if __name__=='__main__':
    solution()