import sys 
from itertools import permutations

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    total = [i for i in range(1,n+1)]
    answer = permutations(total, m)
    for a in answer:
        print(*a)
    
def solution():
    input = sys.stdin.readline
    
    n, m = map(int, input().split())
    
    s = []
    
    def dfs():
        print()
        if len(s) == m:
            print(' '.join(map(str, s)))
            return
        for i in range(1, n+1):
            if i not in s:
               s.append(i)
               print('s append =',s)
               dfs()
               s.pop()
               print('s pop =',s)
               
               
    dfs() 

if __name__=='__main__':
    solution()