import sys 
import copy
from collections import deque

answer = -1e9
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
    
def check(n, m, arr):
    global answer
    tmp = copy.deepcopy(arr)
    q = deque([])
    for i in range(n):
        for j in range(m):
            if tmp[i][j]==2:
                q.append([i,j])
    
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m and tmp[nx][ny]==0:
                tmp[nx][ny]=2
                q.append([nx, ny])
    
    cnt = 0
    for i in range(n):
        cnt += tmp[i].count(0)
    answer = max(answer, cnt)
    
def make_wall(arr, cnt):
    global n, m
    if cnt==3:
        check(n, m, arr)
        return
    
    for x in range(n):
        for y in range(m):
            if arr[x][y]==0:
                arr[x][y]=1
                make_wall(arr, cnt+1)
                arr[x][y]=0
    
def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    
def solution():
    input = sys.stdin.readline
    global n, m
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    make_wall(board, 0)
    print(answer)

if __name__=='__main__':
    mysolution()