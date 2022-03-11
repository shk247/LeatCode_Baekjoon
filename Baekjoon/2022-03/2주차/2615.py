import sys 
from collections import deque
from tkinter import N

def mysolution():
    input = sys.stdin.readline
    board = [list(map(int, input().split())) for _ in range(19)]
    visited = [[0]*19 for _ in range(19)]
    
    dx = [0, 1, -1, 1]
    dy = [1, 0, 1, 1]
    
    def check(i, j, num):
        q = deque()
        q.append([i, j, -1, 1])
        while q:
            x, y, d, cnt = q.popleft()
            visited[x][y] = True
            flag = False
            if d == -1:
                for k in range(3):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0<=nx<19 and 0<=ny<19 and board[nx][ny]==num:
                        q.append([nx, ny, k, cnt+1])
            else:
                nx, ny = x+dx[d], y+dy[d]
                if 0<=nx<19 and 0<=ny<19 and board[nx][ny]==num:
                    flag = True
                    q.append([nx, ny, d, cnt+1])
            
            if cnt==5 and flag==False:
                return True
    
    for i in range(19):
        for j in range(19):
            if board[i][j] == 1 or board[i][j] == 2 and not visited[i][j]:
                if check(i, j, board[i][j]):
                    print(board[i][j])
                    print(i+1, j+1)
                    return
    
    print(0)
    
    
    
def solution():
    input = sys.stdin.readline
    board = [list(map(int, input().split())) for _ in range(19)]
    n = 19 
    
    dx = [0, 1, -1, 1]
    dy = [1, 0, 1, 1]
    
    def omok():
        for x in range(n):
            for y in range(n):
                if board[x][y]:
                    for k in range(4):
                        nx, ny = x+dx[k], y+dy[k]
                        cnt = 1 
                        
                        while 0<=nx<n and 0<=ny<n and board[nx][ny]==board[x][y]:
                            cnt+=1
                            
                            if cnt==5:
                                if 0<=nx+dx[k]<n and 0<=ny+dy[k]<n and board[nx][ny]==board[nx+dx[k]][ny+dy[k]]:
                                    break
                                if 0<=x-dx[k]<n and 0<=y-dy[k]<n and board[x][y]==board[x-dx[k]][y-dy[k]]:
                                    break
                                return  board[x][y], x+1, y+1 
                            
                            nx+=dx[k]
                            ny+=dy[k]
                    
        return 0, -1, -1
        
    color, x, y = omok()
    if not color:
        print(color)
    else:
        print(color)
        print(x, y)
                           
                             
if __name__=='__main__':
    mysolution()