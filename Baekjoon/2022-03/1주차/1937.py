import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    answer = 0 
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def dfs(x, y, num, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]>num:
                dfs(nx, ny, board[nx][ny], cnt+1)
    
    for i in range(n):
        for j in range(n):
            dfs(i, j, board[i][j], 1)
            
    print(answer)

def mysolution2():
    sys.setrecursionlimit(10*100000)
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*n for _ in range(n)]
    answer = 0 
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i+dx[k]
                ny = j+dy[k]
                if 0<=nx<n and 0<=ny<n and board[nx][ny]>board[i][j]:
                    dp[i][j]+=1
                    
    def dfs(x, y, num, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        
        if dp[x][y] == 0:
            return 
        
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]>num:
                dfs(nx, ny, board[nx][ny], cnt+1)
        
    for i in range(n):
        for j in range(n):
            if board[i][j]!=0:
                dfs(i, j, board[i][j], 1)
                
    print(answer)
                    
def solution():
    sys.setrecursionlimit(10*100000)
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*n for _ in range(n)]
    answer = 0 
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def dfs(x, y):
        if dp[x][y]:
            return dp[x][y]
        
        dp[x][y] = 1 
        
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]>board[x][y]:
                dp[x][y] = max(dp[x][y], dfs(nx, ny)+1) 
                
        return dp[x][y]
        
    for i in range(n):
        for j in range(n):
            answer = max(answer, dfs(i, j))
            
    print(answer)

if __name__=='__main__':
    solution()