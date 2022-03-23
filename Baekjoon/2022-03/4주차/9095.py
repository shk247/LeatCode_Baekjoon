import sys 

def mysolution():
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        dp = [0]*12
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, n+1):
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        print(dp[n])
    
def solution():
    input = sys.stdin.readline
    t = int(input())
    
    def fun(num):
        if num == 1:
            return 1
        elif num==2:
            return 2
        elif num == 3:
            return 4
        else:
            return fun(num-1) + fun(num-2) + fun(num-3)
        
    for _ in range(t):
        n = int(input())
        print(fun(n))
        
if __name__=='__main__':
    mysolution()