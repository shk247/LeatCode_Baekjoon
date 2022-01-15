import sys 

def mysolution():
    input = sys.stdin.readline
    sys.setrecursionlimit(100000)
    
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    def dfs(i, j):
        board[i][j] = 0
        for k in range(8):
            _i, _j = i+dx[k], j+dy[k]
            if 0<=_i<h and 0<=_j<w and board[_i][_j] == 1:
                dfs(_i, _j)
        
    while True:
        w, h = map(int, input().split())
        if w == h == 0:
            break
        global board
        board = [list(map(int, input().split())) for _ in range(h)]
        ans = 0 
        for i in range(h):
            for j in range(w):
                if board[i][j]==1:
                    dfs(i, j)
                    ans += 1 
        print(ans)
    
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()