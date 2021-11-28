import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    path = [list(map(int, input().split())) for _ in range(n)]
    answer = [[0]*n]*n
    for i in range(n):
        for j in range(n):
            if i==j:
                answer[i][j] = 1
            elif path[i][j] == 1:
                answer[i][j] = 1
                answer[j][i] = 1

    for i in range(n):
        print(*answer[i])
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    path = [list(map(int, input().split())) for _ in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if path[i][k] and path[k][j]:
                    print('k=',k,'i=',i,'j=',j)
                    path[i][j] = 1
    
    for i in range(n):
        print(*path[i])

if __name__=='__main__':
    solution()