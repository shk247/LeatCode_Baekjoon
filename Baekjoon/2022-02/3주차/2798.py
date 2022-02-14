import sys 
from itertools import combinations

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    answer = 0 
    for l in list(combinations(cards,3)):
        s = sum(l)
        if s<=m:
            answer = max(answer, s)
    print(answer)
            
    
def solution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    cards = list(map(int, input().split()))
    answer = 0 
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                total = cards[i] + cards[j] + cards[k]
                if total <= m:
                    answer = max(answer, total)
                    
    print(answer)
    
if __name__=='__main__':
    mysolution()