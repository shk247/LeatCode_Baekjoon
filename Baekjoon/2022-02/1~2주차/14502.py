import sys 
import copy
from collections import deque

def mysolution():
    input = sys.stdin.readline
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for i in range(n)]
    virus_list = []
    answer = 0 
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                virus_list.append([i, j])
                
    def bfs():
        nonlocal answer
        tmp_board = copy.deepcopy(board)
        q = deque()
        q.extend(virus_list)
        
        while q:
            virus = q.popleft()
            i, j = virus[0], virus[1]
            for k in range(4):
                _i, _j = i+dx[k], j+dy[k]
                if 0<=_i<n and 0<=_j<m and tmp_board[_i][_j]==0:
                    tmp_board[_i][_j]=2
                    q.append([_i, _j])
                            
        cnt = sum(t.count(0) for t in tmp_board)
        answer = max(answer, cnt)
        
    def makeWall(start, num):
        if num==3:
            bfs()
            return
        for x in range(start, n*m):
            i = x//m
            j = x%m
            if board[i][j]==0:
                board[i][j] = 1
                makeWall(x, num+1)
                board[i][j] = 0 
    
    makeWall(0, 0)
    print(answer)

if __name__=='__main__':
    solution()