import sys
from collections import defaultdict, deque
import heapq

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    dict = defaultdict(list)
    for i in range(m):
        a, b, v = map(int, input().split())
        dict[a].append([b, v])

    a, b = map(int, input().split())
    queue = dict[a]
    minimum = 1e9
    while queue:
        print()
        print(queue)
        next, value = queue.pop()
        if next == b:
            minimum = min(minimum, value)
            print('minimum=',minimum)
            continue
        for n, v in dict[next]:
            if v+value<minimum:
                queue.append([n,v+value])
    return minimum
        
def solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    buses = defaultdict(list)
    for _ in range(m):
        x, y, d = list(map(int, input().split()))
        buses[x].append((y, d))
    start, end = list(map(int, input().split()))
    distance = [int(1e9)]*(n+1)
    
    queue = []
    heapq.heappush(queue,(0, start))
    
    while queue:
        dis, now = heapq.heappop(queue)
        
        if distance[now]<dis:
            continue
        
        for bus in buses[now]:
            cost = dis + bus[1]
            if cost < distance[bus[0]]:
                distance[bus[0]] = cost
                heapq.heappush(queue, (cost, bus[0]))
                
    print(distance[end])

if __name__=='__main__':
    print(mysolution())