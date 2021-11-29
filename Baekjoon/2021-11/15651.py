import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    s = []
    def dfs():
        if len(s) == m:
            print(*s)
            return
        for i in range(1, n+1):
            s.append(i)
            dfs()
            s.pop()
    dfs()
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()