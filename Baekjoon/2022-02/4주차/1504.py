import sys 
from collections import deque

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    time = 0 
    shark = 2
    fish_cnt = 0 
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0 -1, 1]
    
    def dfs(i, j):
        nonlocal shark, fish_cnt, time
        time += 1
        tmp = []
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if board[nx][ny]==shark:
                    dfs(nx, ny)
                elif board[nx][ny]<shark:
                    fish_cnt+=1
                    if fish_cnt == shark:
                        shark += 1
                        fish_cnt = 0
                    board[nx][ny]=0
        
    for i in range(n):
        for j in range(n):
            if board[i][j]==9:
                board[i][j]=0
                dfs(i, j)

                    
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    time = 0 
    fish_cnt = 0
    shark = 2 
    shark_x, shark_y = 0, 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j]==9:
                board[i][j]=0
                shark_x, shark_y = i, j
               
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while True:
        q = deque()
        q.append([shark_x, shark_y, 0])
        visited = [[False]*n for _ in range(n)]
        visited[shark_x][shark_y]=True
        eat = []
        while q:
            x, y, move = q.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<n and 0<=ny<n and shark>=board[nx][ny] and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny, move+1])
                    if shark>board[nx][ny] and board[nx][ny]!=0:
                        eat.append([nx, ny, move+1])
        if eat:
            eat.sort(key=lambda x:(x[2], x[0], x[1]))
            x, y, move = eat[0][0], eat[0][1], eat[0][2]
            board[x][y]=0
            shark_x, shark_y = x, y
            time += move
            fish_cnt+=1
            if shark==fish_cnt:
                shark+=1
                fish_cnt=0
        else:
            break
    
    print(time)
    
if __name__=='__main__':
    solution()