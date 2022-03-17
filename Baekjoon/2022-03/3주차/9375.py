import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    m = int(input())
    
    for _ in range(m):
        n = int(input())
    
def solution():
    input = sys.stdin.readline
    m = int(input())
        
    for _ in range(m):
        n = int(input())
        dict = defaultdict(int)
        for _ in range(n):
            a, b = input().split()
            dict[b]+=1
        answer = 1
        for item in dict.keys():
            answer *= (dict[item]+1)    
        
        print(answer-1)
        
if __name__=='__main__':
    solution()