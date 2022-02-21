import sys 

def mysolution():
    input = sys.stdin.readline
    sys.setrecursionlimit(10*100000)
    n = int(input())
    rg_yes = []
    rg_no = []
    
    for _ in range(n):
        tmp = list(input().strip())
        rg_no.append(tmp)
        rg_yes.append(['G' if t=='R' else t for t in tmp ])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def dfs(i, j, arr, check):
        nonlocal n
        arr[i][j]='0'
        for k in range(4):
            ni, nj = i+dx[k], j+dy[k]
            if 0<=ni<n and 0<=nj<n and arr[ni][nj]==check:
                dfs(ni, nj, arr, check)
    
    cnt_yes = 0 
    cnt_no = 0 
    
    for i in range(n):
        for j in range(n):
            if rg_no[i][j] in 'RGB':
                dfs(i, j, rg_no, rg_no[i][j])      
                cnt_no += 1 
            if rg_yes[i][j] in 'GB': 
                dfs(i, j, rg_yes, rg_yes[i][j])     
                cnt_yes += 1
                
    print(cnt_no, cnt_yes)  
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()