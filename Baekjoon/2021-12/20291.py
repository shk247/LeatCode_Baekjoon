import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    dict = defaultdict(int)
    for _ in range(n):
        file = input().strip()
        dict[file.split('.')[1]] += 1
    
    dict = sorted(dict.items())
    
    for k, v in dict:
        print(k, v)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()