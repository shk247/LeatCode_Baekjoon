import sys 

def mysolution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    dp = [0]*(k+1)
    bags = {}
    for _ in range(n):
        w, v = map(int, input().split())
        bags[w] = v
    
    for i in range(1, k+1):
        for bag in bags.keys():
            if i>=bag:
                dp[i] = max(dp[i], bags[bag]+dp[i-bag])
                
    print(dp[k])
            
def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())

    thing = [[0,0]]
    d = [[0]*(k+1) for _ in range(n+1)]

    for i in range(n):
        thing.append(list(map(int, input().split())))

    for i in range(1, n+1):
        for j in range(1, k+1):
            w = thing[i][0]
            v = thing[i][1]

            if j < w:
                d[i][j] = d[i-1][j]
            else:
                d[i][j] = max(d[i-1][j], d[i-1][j-w]+v)

    print(d[n][k])

if __name__=='__main__':
    mysolution()