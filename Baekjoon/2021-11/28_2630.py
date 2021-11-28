import sys 

def check(paper):
    size = len(paper)
    
    if size == 1:
        return  paper.count(0), paper.count(1)

    blue, white = 0, 0 
    for i in range(paper):
        row = paper[i][:size]
        blue += row.count(1)
        white += (size-blue)
    if blue == size or white == size:
        return white, blue
        
    
def mysolution():
    input = sys.stdin.readline
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    # white, blue = 0, 0 
    # for i in range(n):
    #     blue += paper[i].count(1)

    # if blue == n*n or blue == 0:
    #     print(0)
    #     print(1)
    #     return

    white, blue = 0, 0 
    tmp = n 
    while True:
        # 왼쪽 위 
        for i in range(tmp):
            row = paper[i][:tmp]
            blue += row.count(1)
                
        # 오른쪽 위
        # 왼쪽 아래
        # 오른쪽 아래 
        tmp //= 2
        break
    
def solution():
    input = sys.stdin.readline
    N = int(input())
    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 
    result = []
    
    def solution(x, y, n):
        color = paper[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if color != paper[i][j]:
                    solution(x, y, n//2)
                    solution(x, y+n//2, n//2)
                    solution(x+n//2, y, n//2)
                    solution(x+n//2, y+n//2, n//2)
                    return
        if color == 0:
            result.append(0)
        else:
            result.append(1)

    solution(0, 0, N)
    print(result.count(0))
    print(result.count(1))

if __name__=='__main__':
    solution()