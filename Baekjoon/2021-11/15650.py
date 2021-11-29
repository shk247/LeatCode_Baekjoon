import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    s = []
    
    def dfs(start):
        if len(s) == m:
            print(' '.join(map(str, s)))
            return
        for i in range(start, n+1):
            if i not in s:
                s.append(i)
                dfs(i+1)
                s.pop()
    dfs(1)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()