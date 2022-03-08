import sys 

def mysolution():
    input = sys.stdin.readline
    
def solution():
    input = sys.stdin.readline
    n,m = map(int, input().split())

    parent = [set() for _ in range(n+1)]
    child = [set() for _ in range(n+1)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        parent[a].add(b)
        child[b].add(a)
        
    for i in range(1, n+1):
        # 내 부모노드의 자식 노드에 내 자식 노드 추가  
        for j in parent[i]:
            child[j].add(child[i])
        # 내 자식 노드의 부모 노드에 내 부모 노드 추가 
        for j in child[i]:
            parent[j].add(parent[i])
    
    answer = 0 
    for i in range(1, n+1):
        if len(parent[i])+len(child[i]) == n-1:
            answer+=1
            
    print(answer)
        
def solution2():
    N, M = map(int, input().split())
    height = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        height[a][b] = 1
    
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if height[i][k]+height[k][j]==2:
                    height[i][j]=1
    
    answer = 0 
    for i in range(1, N+1):
        tmp = 0 
        for j in range(1, N+1):
            tmp += (height[i][j] + height[j][i])
        if tmp == N-1:
            answer += 1
    print(answer)

if __name__=='__main__':
    mysolution()