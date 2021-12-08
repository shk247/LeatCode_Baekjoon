import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n, d = map(int, input().split())
    roads = defaultdict(list)
    for _ in range(n):
        a, b, c = list(map(int, input().split()))
        roads[a] += [[b, c]]
    now, answer = 0, 0 
    while now<=d:
        if roads[now]:
            road = roads[now]
            road.sort(key=lambda x:(-x[0], x[1]))
            if road[0]<=d:
                now = road[0]
                answer += road[1]
                continue
def solution():
    input = sys.stdin.readline
    n, d = map(int, input().split())
    roads = defaultdict(list)
    for _ in range(n):
        s, e, w = list(map(int, input().split()))
        roads[s] += [[w, e]]
    distance = [i for i in range(d+1)]
    
    for i in range(d+1):
        if i!=0:
            distance[i] = min(distance[i], distance[i-1]+1)
        for w, e in roads[i]:
            if e<=d and distance[e] > w+distance[i]:
                distance[e] = w + distance[i]
    print(distance[d])
if __name__=='__main__':
    solution()