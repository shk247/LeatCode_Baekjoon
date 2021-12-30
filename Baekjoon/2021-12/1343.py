import sys 

def mysolution():
    input = sys.stdin.readline
    board = input().strip()
    board = board.replace('XXXX','AAAA').replace('XX','BB')
    if 'X' in board:
        print(-1)
    else:
        print(board)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()