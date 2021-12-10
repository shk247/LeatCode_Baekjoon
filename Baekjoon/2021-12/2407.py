import collections
import sys 
from itertools import combinations
import math 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    nums = [i for i in range(n)]
    print(len(list(combinations(nums, m))))
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    up = math.factorial(n)
    down = (math.factorial(n-m)) * (math.factorial(m))
    print(up//down)

def solution2():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    
    fac = [1, 1, 2]
    for i in range(3, n):
        fac.append(fac[i-1] * i)

    print(fac[n]//(fac[n-m]*fac[m]))
    
if __name__=='__main__':
    mysolution()