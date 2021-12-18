import sys 

def mysolution():
    input = sys.stdin.readline
    r, c = map(int, input().split())
    board = [list(input().strip()) for _ in range(r)]
    answer = 1 
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'S':
                # 위
                if i>0 and board[i-1][j] == 'W':
                    answer = 0
                    break
                # 아래
                if i<r-1 and board[i+1][j] == 'W':
                    answer = 0
                    break
                # 왼쪽
                if j>0 and board[i][j-1] == 'W':
                    answer = 0
                    break
                # 오른쪽 
                if j<c-1 and board[i][j+1] == 'W':
                    answer = 0
                    break
            elif board[i][j] == '.':
                board[i][j] = 'D'
        if j!=c-1:
            break
        
    print(answer)
    
    if answer:       
        for b in board:
            print(''.join(b))
        
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()