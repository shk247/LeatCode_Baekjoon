import sys 

def mysolution():
    input = sys.stdin.readline
    n, r, c = map(int, input().split())
    n = 2**n
    
    num = 0 
    board = [[0]*n for _ in range(n)]
    
    dx = [0, 0, 1, 1]
    dy = [0, 1, 0, 1]
    
    def fun(n, x, y):
        nonlocal num
        if n==2:
            for k in range(4):
                board[x+dx[k]][y+dy[k]] = num
                num += 1
        else:
            n //= 2
            fun(n, x, y)
            fun(n, x, y+n)
            fun(n, x+n, y)
            fun(n, x+n, y+n)
    
    fun(n, 0, 0)
    
    print(board[r][c])
    
def mysolution2():
    input = sys.stdin.readline
    n, r, c = map(int, input().split())
    n = 2**n
    
    num = 0 
    
    dx = [0, 0, 1, 1]
    dy = [0, 1, 0, 1]
    
    def fun(n, x, y):
        nonlocal num, r, c
        if n==2:
            for k in range(4):
                nx, ny = x+dx[k], y+dy[k]
                if nx==r and ny==c:
                    print(num)
                    exit()
                num += 1
        else:
            n //= 2
            fun(n, x, y)
            fun(n, x, y+n)
            fun(n, x+n, y)
            fun(n, x+n, y+n)
    
    fun(n, 0, 0)
    
def solution():
    input = sys.stdin.readline
    n, r, c = map(int, input().split())
    ans = 0 
    
    while n!=0:
        n-=1
        sqare = 2**n
        if r<sqare and c<sqare:
            pass
        elif r<sqare and c>=sqare:
            ans += sqare * sqare 
            c-=sqare
        elif r>=sqare and c<sqare:
            ans += sqare * sqare * 2
            r-=sqare
        else:
            ans += sqare * sqare * 3
            r-=sqare
            c-=sqare
    
    print(ans) 
    
    
def solution():
    input = sys.stdin.readline
    n, r, c = map(int, input().split())
    result = 0

    def z(n, x, y):
        nonlocal result
        if x == r and y == c:
            print(int(result))
            exit(0)

        if n == 1:
            result += 1
            return

        if not (x <= r < x + n and y <= c < y + n):
            result += n * n
            return
        z(n / 2, x, y)
        z(n / 2, x, y + n / 2)
        z(n / 2, x + n / 2, y)
        z(n / 2, x + n / 2, y + n / 2)

    z(2 ** n, 0, 0)
    
if __name__=='__main__':
    mysolution2()