import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    city = [[1e9] * n for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        if city[a-1][b-1] > c:
            city[a-1][b-1] = c
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i!=j and city[i][k]+city[k][j]<city[i][j]:
                    city[i][j]=city[i][k]+city[k][j]
                   
    for i in city:
        for j in i:
            if j == 1e9:
                print(0, end=' ')
            else:
                print(j, end=' ')
        print()
            
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()