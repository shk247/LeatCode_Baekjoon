import sys 
from collections import Counter

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    for i in range(n):
        for j in range(1, n):
            if board[i][j] != board[i][j-1]:
                board[i][j], board[i][j-1] = board[i][j-1], board[i][j]
    ans = 0 
    for i in range(n):
        tmp = Counter(board[i])
        ans = max(ans, tmp.most_common()[0][1])
    
    board = list(map(list, zip(*board)))
    for i in range(n):
        tmp = Counter(board[i])
        ans = max(ans, tmp.most_common()[0][1])
        
    print(ans)
    
def check(arr):
    n = len(arr)
    answer = 1 
    # 행 순회
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if arr[i][j] == arr[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt)
    # 열 순회
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if arr[j][i] == arr[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            answer = max(answer, cnt) 
    
    return answer
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(input().strip()) for _ in range(n)]
    answer = 0 
    # 행 변경 
    for i in range(n):
        for j in range(n-1):
            if board[i][j] != board[i][j+1]:
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
                tmp = check(board)
                answer = max(tmp, answer)
                board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
    # 열 변경
    for i in range(n):
        for j in range(n-1):
            if board[j][i] != board[j+1][i]:
                board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
                tmp = check(board)
                answer = max(tmp, answer)
                board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
                
    print(answer)

if __name__=='__main__':
    solution()