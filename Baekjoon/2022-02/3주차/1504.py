import heapq
import sys 
from heapq import heappop, heappush, heappushpop
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n, e = map(int, input().split())
    edges = defaultdict(list)
    
    for _ in range(e):
        a, b, c =  map(int, input().split())
        edges[a].append([c, b])
        edges[b].append([c, a])
        
    a, b = map(int, input().split())
    
    def dij(start):
        board = [1e9 for _ in range(n+1)]
        board[start] = 0 
        q = []
        heappush(q, [0, start])
        
        while q:
            cost, node = heappop(q)
            for edge in edges[node]:
                cost2, node2 = edge
                if board[node2] > cost + cost2:
                    board[node2] = cost + cost2
                    heappush(q, [cost+cost2, node2])

        return board
    
    s_board = dij(1)
    a_board = dij(a)    
    b_board = dij(b)
    
    answer = 1e9
    answer = min(s_board[a]+a_board[b]+b_board[n], s_board[b]+b_board[a]+a_board[n])
    
    if answer < 1e9:
        print(answer)
    else:
        print(-1)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()