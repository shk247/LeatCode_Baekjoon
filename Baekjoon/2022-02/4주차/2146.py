from collections import deque
import sys
import heapq

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def dfs(i, j, arr, num):
        arr[i][j] = num
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
                dfs(nx, ny, arr, num)
    
    change_num = 2
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                dfs(i, j, board, change_num)
                change_num += 1
                
    bridge = 1e9 
    
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0:
                flag = False
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]==0:
                        flag = True
                if flag:
                    q = []
                    heapq.heappush(q, [0, [i, j]])
                    check = board[i][j]
                    while q:
                        move, point = heapq.heappop(q);
                        x, y = point[0], point[1]
                        for k in range(4):
                            nx = x + dx[k]
                            ny = y + dy[k]
                            if 0<=nx<n and 0<=ny<n and board[nx][ny]!=check:
                                if board[nx][ny]>check:
                                    bridge = min(bridge, move)
                                    break
                                elif board[nx][ny]==0:
                                    heapq.heappush(q, [move+1, [nx, ny]])
                        else:
                            continue
                        
                        break
    
def solution():
    sys.setrecursionlimit(10*100000)
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def dfs(i, j, arr, num):
        arr[i][j] = num
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0<=nx<n and 0<=ny<n and arr[nx][ny]==1:
                dfs(nx, ny, arr, num)
    
    change_num = 2
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                dfs(i, j, board, change_num)
                change_num += 1
                
    bridge = 1e9 
    
    def bfs(num):
        nonlocal bridge
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        
        for i in range(n):
            for j in range(n):
                if board[i][j]==num:
                    q.append([i, j])
                    dist[i][j]=0
                    
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0<=nx<n and 0<=ny<n:
                    if board[nx][ny]>num:
                        bridge = min(bridge, dist[x][y])
                        return
                    elif board[nx][ny]==0 and dist[nx][ny]==-1:
                        dist[nx][ny] = dist[x][y]+1
                        q.append([nx, ny])
    
    for i in range(2, change_num):
        bfs(i)
        
    print(bridge)

if __name__=='__main__':
    solution()