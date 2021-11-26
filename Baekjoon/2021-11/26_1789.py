import sys 

def mysolution():
    input = sys.stdin.readline
    _max = int(input())
    n = 1
    while (n*(n+1))/2<=_max:
        n+=1
    return n-1

def solution():
    input = sys.stdin.readline
    return

if __name__=='__main__':
    mysolution()