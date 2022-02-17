from collections import deque
import sys 
import copy 

def mysolution_dfs():
    sys.setrecursionlimit(10*100000)
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    answer = 0
    
    def dfs(x, y, arr, check):
        arr[x][y] = 0 
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny]>check:
                dfs(nx, ny, arr, check)
        
    for k in range(100):
        arr = copy.deepcopy(board)
        cnt = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j]>k:
                    dfs(i, j, arr, k)
                    cnt += 1
        if cnt==0:
            break
        answer = max(answer, cnt)
        
    print(answer)
    
def mysolution_bfs():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    answer = 0
    
    for k in range(100):
        arr = copy.deepcopy(board)
        cnt = 0
        for i in range(n):
            for j in range(n):
                if arr[i][j] > k:
                    cnt+=1
                    q = deque()
                    q.append([i, j])
                    arr[i][j] = 0 
                    while q:
                        x, y = q.popleft()
                        for m in range(4):
                            nx, ny = x+dx[m], y+dy[m]
                            if 0<=nx<n and 0<=ny<n and arr[nx][ny]>k:
                                arr[nx][ny] = 0 
                                q.append([nx, ny])
        if cnt==0:
            break
        answer = max(answer, cnt)
        
    print(answer)
        
        
def solution():
    input = sys.stdin.readline
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    graph_min = min(map(min, graph))
    graph_max = max(map(max, graph))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    max_safe_area = 0   
    
    def bfs(x, y, safe_area):    # BFS implementation
        queue = deque()
        queue.append((x, y))
        visited[x][y] = 1	# visited mark
    
        while queue:
            x, y = queue.popleft()
    
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
    
                if 0 <= nx < N and 0 <= ny < N:
                    if graph[nx][ny] >= safe_area and visited[nx][ny] == 0:    
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                    
    for safe_area in range(graph_min, graph_max+1):
        visited = [[0] * N for _ in range(N)]
        temp = 0
        for i in range(N):
            for j in range(N):
                if graph[i][j] >= safe_area and visited[i][j] == 0:
                    bfs(i, j, safe_area)
                    temp += 1
        max_safe_area = max(max_safe_area, temp)
        
    print(max_safe_area)
    
if __name__=='__main__':
    mysolution_bfs()