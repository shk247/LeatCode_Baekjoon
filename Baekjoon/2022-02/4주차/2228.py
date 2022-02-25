import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = [int(input()) for _ in range(n)]

    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    con = [[0]+[-1e9]*m for _ in range(n+1)]
    notcon = [[0]+[-1e9]*m for _ in range(n+1)]
    
    for i in range(1, n+1):
        num = int(input())
        for j in range(1, m+1):
            notcon[i][j] = max(notcon[i-1][j], con[i-1][j])
            con[i][j] = max(notcon[i-1][j-1], con[i-1][j]) + num
    
    print(max(con[n][m], notcon[n][m]))

if __name__=='__main__':
    solution()