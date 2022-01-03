import sys 

def check(n, arr):
    zero_cnt = 0 
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                zero_cnt += 1
    return n//2==zero_cnt

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    
def solution():
    input = sys.stdin.readline
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    global zero_cnt, one_cnt
    zero_cnt = one_cnt = 0 
    def solution(x, y, n):
        global zero_cnt, one_cnt
        color = board[x][y]
        for i in range(x, x+n):
            for j in range(y, y+n):
                if color != board[i][j]:
                    _n = n//2
                    solution(x, y, _n)
                    solution(x, y+_n, _n)
                    solution(x+_n, y, _n)
                    solution(x+_n, y+_n, _n)
                    return
        if color == 1:
            one_cnt+=1
        else:
            zero_cnt+=1
    
    solution(0, 0, n)
    print(zero_cnt)
    print(one_cnt)

if __name__=='__main__':
    mysolution()