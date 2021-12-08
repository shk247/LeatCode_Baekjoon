import sys 
from collections import Counter, defaultdict

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    total = [input().strip() for _ in range(n)]
    finish = [input().strip() for _ in range(n-1)]
    answer = Counter(total)-Counter(finish)
    print(list(answer)[0])
        
def solution():
    input = sys.stdin.readline
    n = int(input())
    person = defaultdict(int)
    finish = defaultdict(int)
    
    for _ in range(n):
        person[input().strip()] += 1
    for _ in range(n-1):
        person[input().strip()] -= 1
    
    print([k for k,v in person.items() if v==1][0])

if __name__=='__main__':
    solution()