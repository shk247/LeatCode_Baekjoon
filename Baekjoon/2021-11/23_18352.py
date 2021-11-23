import sys 
from collections import defaultdict, deque

def mysolution():
    input = sys.stdin.readline
    n, m, k, x = map(int, input().strip().split(' '))
    dis = [0]*n
    # roads = defaultdict(list)
    roads = []
    
    for _ in range(m):
        a, b = map(int, input().strip().split(' '))
        # roads[a].append(b)
        roads.append([a,b])
        
    for a,b in roads:
        print('a=',a,'b=',b)
        print('dis=',dis)
        if dis[a]>0:
            dis[b] = min(dis[b], dis[a]+1)
        else:
            dis[b] = 1
    
    print('dis=',dis)
        

def solution():
    input = sys.stdin.readline
    n, m, k, x = map(int, input().split(' '))
    path = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, input().split(' '))
        path[a].append(b)
        
    answer = [-1] * (n+1)
    answer[x] = 0 
    q = deque([x])
    
    while q:
        town = q.popleft()
        for i in path[town]:
            if answer[i] == -1:
                answer[i] = answer[town] + 1 
                q.append(i)
                
    if k not in answer:
        print(-1)
    else:
        for i in range(n+1):
            if answer[i]==k:
                print(i)

if __name__=='__main__':
    solution()