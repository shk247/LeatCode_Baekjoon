import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    t=[1, 1, 2, 5]
    for i in range(4, n+1):
        a, b = 0, i-1
        tmp = 0
        while b>=0:
            tmp += t[a]*t[b]
            b-=1
            a+=1
        t.append(tmp)
    print(t[n])
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    dp = [0]*(n+1)
    
    def t(n):
        if not n:
            return 1
        if not dp[n]:
            for i in range(n):
                dp[n] += t(i) * t(n-i-1)
        return dp[n]

if __name__=='__main__':
    mysolution()