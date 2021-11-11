from collections import defaultdict
import heapq

def solution():
    n = int(input())
    m = int(input())
    buses = defaultdict(list)
    for _ in range(m):
        x, y, d = list(map(int, input().split()))
        buses[x].append((y, d))
    start, end = list(map(int, input().split()))
    distance = [int(1e9)]*(n+1)
    
    def dij(start):
        queue = []
        heapq.heappush(queue, (0, start))
        
        while queue:
            dist, now = heapq.heappop(queue)
            
            if distance[now]<dist:
                continue
            
            for bus in buses[now]:
                cost = dist + bus[1]
                if distance[bus[0]] > cost:
                    distance[bus[0]] = cost
                    heapq.heappush(queue, (cost, bus[0]))
                    
    dij(start)
    print(distance[end])
        

if __name__ == '__main__':
    solution()
    