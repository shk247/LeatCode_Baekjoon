import sys 
from collections import deque

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    shark_x, shark_y = 0, 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                shark_x, shark_y = i, j
                board[i][j] = 0
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    shark = 2
    eat_fish = 0 
    time = 0 
    
    while True:
        q = deque()
        q.append([shark_x, shark_y, 0])
        visited = [[False]*n for _ in range(n)]
        visited[shark_x][shark_y] = 1
        fish = []
            
        while q:
            x, y, cnt = q.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<n and 0<=ny<n and board[nx][ny] <= shark and visited[nx][ny]==False:
                    visited[nx][ny] = True
                    q.append([nx, ny, cnt+1])
                    if board[nx][ny] != 0 and board[nx][ny] < shark:
                        fish.append([nx, ny, cnt+1])
                        
        if fish:
            fish.sort(key=lambda x: (x[2],x[0],x[1]))
            x, y, move = fish[0][0], fish[0][1], fish[0][2]
            time += move
            eat_fish += 1
            board[x][y] = 0 
            if eat_fish == shark:
                shark += 1
                eat_fish = 0 
            shark_x, shark_y = x, y
        else:
            break
    
    print(time)
            
def solution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
    shark_x, shark_y = 0, 0
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                shark_x, shark_y = i, j
                board[i][j] = 0
    
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    
    shark = 2
    eat_fish = 0 
    time = 0 
    
    while True:
        q = deque()
        q.append([shark_x, shark_y, 0])
        visited = [[False]*n for _ in range(n)]
        fish = []
        flag = 1e9
            
        while q:
            x, y, count = q.popleft()

            if count > flag:
                break
            for k in range(4):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    continue
                if board[nx][ny] > shark or visited[nx][ny]:
                    continue

                if board[nx][ny] != 0 and board[nx][ny] < shark:
                    fish.append((nx, ny, count + 1))
                    flag = count
                visited[nx][ny] = True
                q.append((nx, ny, count + 1))
                        
        if fish:
            fish.sort()
            x, y, move = fish[0][0], fish[0][1], fish[0][2]
            time += move
            eat_fish += 1
            board[x][y] = 0 
            if eat_fish == shark:
                shark += 1
                eat_fish = 0 
            shark_x, shark_y = x, y
        else:
            break
    
    print(time)

if __name__=='__main__':
    mysolution()