import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    
    dict = defaultdict(int)
    startday = 1e9 
    lastday = 0 
    for _ in range(n):
        a, b = map(int, input().split())
        startday = min(startday, a)
        lastday = max(lastday, b)
        for i in range(a, b+1):
            dict[i]+=1
        
    answer = 0 
    col = row = 0     
    for day in range(startday, lastday+2):
        if dict[day] == 0:
            answer += (row*col)
            col = row = 0
        else:
            col += 1
            row = max(row, dict[day])
    
    print(answer)
        
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()