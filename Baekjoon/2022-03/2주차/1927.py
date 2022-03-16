import sys 
import heapq

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    q = []
    for _ in range(n):
        x = int(input())
        if x==0:
            if not q:
                print(0)
            else:
                print(heapq.heappop(q))
        else:
            heapq.heappush(q, x)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()