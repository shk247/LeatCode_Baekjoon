import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    # 정점의 수, 루트 번호, 쿼리 수 
    n, r, q = map(int, input().split())
    sub = [0]*(n+1)
    
    dict = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
    
def solution():
    input = sys.stdin.readline
    # 정점의 수, 루트 번호, 쿼리 수 
    n, r, q = map(int, input().split())
    sub = [0]*(n+1)
    
    dict = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
    
    def findsubtree(node):
            sub[node] = 1 
            for n in dict[node]:
                if not sub[n]:
                    findsubtree(n)
                    sub[node] += sub[n]
    
    findsubtree(r)
    
    for _ in range(q):
        u = int(input())
        print(sub[u])

if __name__=='__main__':
    mysolution()