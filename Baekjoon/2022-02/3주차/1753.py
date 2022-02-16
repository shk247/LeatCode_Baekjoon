import sys 
from collections import defaultdict
import heapq

def mysolution():
    input = sys.stdin.readline
    v, e = map(int, input().split())
    start = int(input())
    dict = defaultdict(list)
    
    for _ in range(e):
        a, b, w = map(int, input().split())
        dict[a].append([w, b])
    
    q = []
    heapq.heappush(q, [0, start])
    dij = [1e9] * (v+1)
    dij[start] = 0 
    
    while q:
        print(q)
        cost, node = heapq.heappop(q)
        for i in dict[node]:
            if dij[i[1]]>=cost+i[0]:
                dij[i[1]]=cost+i[0]
                heapq.heappush(q, [cost+i[0], i[1]])
    for i in range(1, v+1):
        if dij[i]==1e9:
            print('INF')
        else:
            print(dij[i])
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()