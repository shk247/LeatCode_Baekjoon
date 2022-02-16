import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    board = [[1e9]*n for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        if board[a-1][b-1] > c:
            board[a-1][b-1] = c
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i!=j and board[i][j] > board[i][k] + board[k][j]:
                    board[i][j] = board[i][k] + board[k][j]
    
    for row in board:
        for col in row:
            if col==1e9:
                print(0, end=' ')
            else:
                print(col, end=' ')
        print()
        
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()