import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split(' '))
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split(' '))))
    
    k = int(input())
    
    for _ in range(k):
        x1, y1, x2, y2 =  map(int, input().split(' '))
        total = 0 
        for i in range(x1-1,x2):
            for j in range(y1-1, y2):
                total += arr[i][j]
        print(total)

def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = []
    dp = [[0]*(m+1) for _ in range(n+1)]
    for _ in range(n):
        a.append(list(map(int, input().split())))
    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = a[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
            
    k = int(input())
    
    for _ in range(k):
        i,j,x,y = map(int, input().split())
        print(dp[x][y]-dp[x][j-1] - dp[i-1][y]+dp[i-1][j-1])

if __name__=='__main__':
    mysolution()