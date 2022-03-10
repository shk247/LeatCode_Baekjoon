import sys 
import copy

def mysolution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    d = list(map(int, input().split()))
    p = copy.deepcopy(s)

    for _ in range(k%(n-1)):    
        tmp = copy.deepcopy(p)
        for i in range(n):
            p[d[i]-1] = tmp[i]
    
    print(' '.join(map(str, p)))
    
def solution():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    d = list(map(int, input().split()))

    for _ in range(k):    
        tmp = [0]*n
        for i in range(n):
            tmp[d[i]-1] = s[i]
        s = tmp
    
    print(' '.join(map(str, s)))

if __name__=='__main__':
    mysolution()