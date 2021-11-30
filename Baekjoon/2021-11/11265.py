import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    parties = [list(map(int, input().split())) for _ in range(n)] 
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if parties[i][j] > parties[i][k] + parties[k][j]:
                    parties[i][j] = parties[i][k] + parties[k][j]
    
    for _ in range(m):
        a, b, c = map(int, input().split())
        if parties[a-1][b-1] <= c:
            print('Enjoy other party')
        else:
            print('Stay here')
            
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()