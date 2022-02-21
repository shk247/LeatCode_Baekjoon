import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n, r, q = map(int, input().split())
    tree = defaultdict(list)
    
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)            
        
    cnt = [0]*(n+1)
    
    def dfs(node):
        cnt[node] = 1
        for n in tree[node]:
            if not cnt[n]:
                dfs(n)
                cnt[node] += cnt[n]
    dfs(r)
    
    for _ in range(q):
        print(cnt[int(input())])
    
def solution():
    input = sys.stdin.readline
    n, r, q = map(int, input().split())
    tree = defaultdict(list)
    count = [0]*(n+1)
    for _ in range(n-1):
        a, b = map(int, input().split())
        tree[a].append(b)        
        tree[b].append(a)
        
    def cntPoint(x):
        count[x]=1
        for i in tree[x]:
            if not count[i]:
                cntPoint(i)
                count[x]+=count[i]
                
    cntPoint(r)        
    
    for _ in range(q):
        u = int(input())
        print(count[u])
    
if __name__=='__main__':
    mysolution()