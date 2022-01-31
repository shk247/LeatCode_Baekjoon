import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    dp = [0, 1, 1]
    
    for _ in range(3, n+1):
        dp.append(dp[-1]+dp[-2])
        
    print(dp[n])
    
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()