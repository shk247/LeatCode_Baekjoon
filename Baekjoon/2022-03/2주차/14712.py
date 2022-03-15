import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    answer = 2**(n*m)
    
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    
    for x in range(n):
        for y in range(m):
            cnt = 0 
            for k in range(3):
                if 0<=x+dx[k]<n and 0<=y+dy[k]<n:
                    cnt+=1
            if cnt==3:
                answer -= ()

    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    graph = [[0] * (m + 1) for _ in range(n + 1)]
    count = 0
    
    def dfs(x, y):
        nonlocal count
        
        if (x,y) == (1,n+1):
            count += 1
            return
        
        if x == m:
            nx, ny = 1, y+1
        else:
            nx, ny = x+1, 1
            
        dfs(nx, ny)
        
        if graph[y-1][x]==0 or graph[y][x-1]==0 or graph[y-1][x-1] == 0:
            graph[y][x] = 1
            dfs(nx, ny)
            graph[y][x] = 0 
            
    dfs(1, 1)
    
    print(count)
            

if __name__=='__main__':
    mysolution()