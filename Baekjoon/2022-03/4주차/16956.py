import sys 

def mysolution():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    parm = [list(input().rstrip()) for _ in range(r)]
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    def check(parm, i, j):
        nonlocal r, c
        for k in range(4):
            nx, ny = i+dx[k], j+dy[k]
            if 0<=nx<r and 0<=ny<c:
                if parm[nx][ny]=='W':
                    return False
                elif parm[nx][ny]=='.':
                    parm[nx][ny]='D'
        return True
    
    flag = True
    for i in range(r):
        for j in range(c):
            if parm[i][j]=='S':
                if not check(parm, i, j):
                    flag = False
                    break
        if not flag:
            break     
    
    if flag:
        print(1)
        for p in parm:
            print(''.join(p))   
    else:
        print(0)
                            
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()