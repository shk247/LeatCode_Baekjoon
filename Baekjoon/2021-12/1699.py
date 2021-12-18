import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    
    def check(num):
        if num==1:
            return 1
        
        n = 1
        while n**2<=num:
            n+=1
        n-=1
        
        result = num-(n**2)
        
        if result==0:
            return 1
        else:
            return 1+check(result)
    
    
    print(check(n))
        
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    dp = [i for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n):
            if j*j>i:
                break
            if dp[i]>dp[i-j*j] + 1:
                dp[i] = dp[i-j*j] + 1
    print(dp[n])

if __name__=='__main__':
    mysolution()