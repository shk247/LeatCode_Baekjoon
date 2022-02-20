import sys 
from  collections import defaultdict, deque

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    dict = defaultdict(list)
    indgree = [0]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        dict[a].append(b)
        indgree[b] += 1
        
    q = deque()
    for i in range(1, n+1):
        if indgree[i]==0:
            q.append(i)
            
    while q:
        a = q.popleft()
        for b in dict[a]:
                indgree[b]-=1
                if indgree[b]==0:
                    q.append(b)
        print(a,end=' ')
        
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()