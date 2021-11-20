def mysolution():
    n = int(input())
    roads = [int(input()) for _ in range(n-1)]
    costs = [int(input()) for _ in range(n)]

    total = sum(roads)
    answer = []
    
    for i in range(n-1):
        for j in range(n):
            pass
        
def solution():
    n = int(input())
    roads = list(map(int, input().split()))
    costs = list(map(int, input().split()))
    
    m = costs[0]
    sum = 0 
    
    for i in range(n-1):
        if m > costs[i]:
            m = costs[i]
        sum += (m*roads[i])
        
    print(sum)


if __name__=='__main__':
    solution()