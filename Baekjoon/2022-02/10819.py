import sys 
from itertools import permutations

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    answer = 0 
    nums = list(map(int, input().split()))
    for l in list(permutations(nums, n)):
        tmp = 0
        for i in range(0, len(l)-1):
            tmp += abs(l[i]-l[i+1])
        answer = max(answer, tmp)
        
    print(answer) 
    
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()