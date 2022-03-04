import sys 

def mysolution():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    
    
def solution():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(r)]
    answer = 0 
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    alphas = set()
    alphas.add(maps[0][0])
    
    def dfs(x, y, cnt):
        nonlocal answer
        answer = max(answer, cnt)
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<r and 0<=ny<c and maps[nx][ny] not in alphas:
                alphas.add(maps[nx][ny])
                dfs(nx, ny, cnt+1)
                alphas.remove(maps[nx][ny])
                        
    dfs(0, 0, 1)
    
    return answer

if __name__=='__main__':
    mysolution()