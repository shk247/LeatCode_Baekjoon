import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline

def solution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10 ** 9) 
    n = int(input()) 
    lines = defaultdict(list)
    for _ in range(n - 1): 
        a, b = map(int, input().split()) 
        lines[a].append(b) 
        lines[b].append(a) 
    dp = [[0, 0] for _ in range(n + 1)] 
    visited = [0 for _ in range(n + 1)]
    
    def dfs(node):
        visited[node] = True
        dp[node][0] = 1
        for i in lines[node]:
            if not visited[i]:
                dfs(i)
                # node가 얼리어답터일 때 서브 트리에서 얼리어답터의 최소값
                dp[node][0] += min(dp[i][0], dp[i][1])
                # node가 얼리어답터가 아닐 때 서브 트리에서 얼리어탑터의 최소값 
                dp[node][1] += dp[i][0]
                
    dfs(1)
    print(min(dp[1][0], dp[1][1]))
    
if __name__=='__main__':
    mysolution()