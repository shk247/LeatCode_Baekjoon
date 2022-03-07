from collections import deque
import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    time = 0
    dx = [-1, 1, 0, 0]
    dt = [0, 0, -1, 1]
    
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    time = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while True:
        q = deque()
        visited = [[0 for _ in range(m)] for _ in range(n)]
        visited[0][0] = 1 
        q.append([0, 0])
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny]: 
                    if board[nx][ny]:
                        board[nx][ny]+=1
                    else:
                        visited[nx][ny]=1
                        q.append([nx, ny])
        flag = 0 
        for i in range(n):
            for j in range(m):
                if board[i][j]>=3:
                    board[i][j]=0
                elif 0<board[i][j]:
                    flag=1
                    board[i][j]=1
        time+=1
        
        if not flag:
            print(time)
            break

if __name__=='__main__':
    mysolution()