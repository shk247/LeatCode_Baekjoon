import sys 
import copy

def mysolution():
    sys.setrecursionlimit(100000)
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    nums = []
    for i in range(n):
        nums.extend(board[i])
    nums = list(set(nums))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    answer = 1
     
    def dfs(board, num, x, y):
        nonlocal n
        board[x][y] = 0 
        for k in range(4):
            _x, _y = x+dx[k], y+dy[k]
            if 0<=_x<n and 0<=_y<n and board[_x][_y]>num:
                dfs(board, num, _x, _y)
    
    for num in nums:
        tmp = 0 
        tmp_board = copy.deepcopy(board)
        for i in range(n):
            for j in range(n):
                if tmp_board[i][j]>num:
                    dfs(tmp_board, num, i, j)
                    tmp += 1
        answer = max(answer, tmp)
        
    print(answer)
                    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()