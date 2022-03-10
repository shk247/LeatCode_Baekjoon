import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    members = list(map(int, input().split()))
    dict = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    members = [0] + list(map(int, input().split()))
    dict = defaultdict(list)
    for _ in range(n-1):
        a, b = map(int, input().split())
        dict[a].append(b)
        dict[b].append(a)

    visited = [False] * (n+1)
    dp = [[0]*2 for i in range(n+1)]
    
    def dfs(node):
        visited[node]=True
        dp[node][1]=members[node]
        for n in dict[node]:
            if not visited[n]:
                dfs(n)
                dp[node][1] += dp[n][0]
                dp[node][0] += max(dp[n][0], dp[n][1])
    
    dfs(1)
    print(max(dp[1][1], dp[1][0]))
    
if __name__=='__main__':
    solution()