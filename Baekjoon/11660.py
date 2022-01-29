import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(n)]
    arr = [[] for _ in range(n+1)]
    
    def fun(x, y):
        answer = 0 
        for i in range(x):
            for j in range(y):
                answer += board[i][j]
        return answer
    
    for i in range(n+1):
        for j in range(n+1):
            arr[i].append(fun(i, j))

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(arr[x2][y2]-arr[x1-1][y2]-arr[x2][y1-1]+arr[x1-1][y1-1])
    
def solution():
    input = sys.stdin.readline
    n, m = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]+board[i-1][j-1]
            
    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])        
            
if __name__=='__main__':
    mysolution()