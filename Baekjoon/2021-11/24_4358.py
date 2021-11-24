import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    dict = defaultdict(int)
    cnt = 0 
    while True:
        n = input().strip()
        if not n:
            break
        dict[n] += 1
        cnt += 1
        
    dict = sorted(dict.items())
    
    for d in dict:
        num = round((d[1]/cnt)*100, 4)
        print(d[0],'%.4f'%num)

def solution():
    input = sys.stdin.readline
    return

if __name__=='__main__':
    mysolution()