import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    dict = defaultdict(list)
    
    for _ in range(n):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
    
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    dict = defaultdict(list)
    
    for _ in range(n):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
        
    dp = [[0, 0] for _ in range(n+1)]
    visited = [False] * (n+1)
    
    def dfs(node):
        visited[node] = True
        dp[node][0] = 1 
        
        for node2 in dict[node]:
            if not visited[node2]:
                dfs(node2)
                dp[node][0] += min(dp[node2][0], dp[node2][1])
                dp[node][1] += dp[node][0]
        
    dfs(1)
    print(min(dp[0][0], dp[0][1]))
    
if __name__=='__main__':
    mysolution()