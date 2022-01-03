import sys 
from itertools import permutations

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = [i for i in range(1,n+1)]
    com = list(permutations(nums, m))
    for c in com:
        print(' '.join(map(str, c)))
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    s = []
    def f(s):
        if len(s)==m:
            print(' '.join(map(str, s)))
            return
        for i in range(1, n+1):
            if i in s:
                continue
            s.append(i)
            f(s)
            s.pop()
    f(s)

if __name__=='__main__':
    mysolution()