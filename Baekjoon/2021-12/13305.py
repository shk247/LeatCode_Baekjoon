import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    length = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    minimun = 1e9
    
    
            
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    roads = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    minimun = prices[0]
    res = roads[0]*minimun
    
    for i in range(1, len(roads)):
        minimun = min(minimun, prices[i])
        res += roads[i]*minimun
    
    print(res)
        

if __name__=='__main__':
    solution()