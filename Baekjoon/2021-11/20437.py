import sys
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    t = int(input())
    
    for _ in range(t):
        w = input().strip()
        k = int(input())
        l = defaultdict(list)

        for i in range(len(w)):
            if w.count(w[i])>=k:
                l[w[i]].append(i)
        
        if not l:
            print(-1)
            continue
        print(l)
        min_str = 10000
        max_str = 0
        for lst in l.values():
            for j in range(len(lst)-k+1):
                tmp = lst[j+k-1]-lst[j]+1
                min_str = min(min_str,tmp)
                max_str = max(max_str,tmp)
                
        print(min_str, max_str)
                
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()