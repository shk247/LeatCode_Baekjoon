import sys 
from itertools import combinations

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    result = 0 
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                tmp = cards[i]+cards[j]+cards[k]
                if tmp <= m:
                    result = max(result, tmp)
                    
    print(result)
    
def solution2():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    result = 0
    
    for com in combinations(cards, 3):
        tmp = sum(com)
        if tmp <= m:
            result = max(result, tmp)
                    
    print(result)       

if __name__=='__main__':
    mysolution()