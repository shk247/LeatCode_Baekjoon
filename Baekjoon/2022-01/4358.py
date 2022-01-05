import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    dict = defaultdict(int)
    cnt = 0
    while True:
        word = input().strip()
        if not word:
            break
        cnt += 1
        dict[word] += 1
    
    dict = sorted(dict.items(), key=lambda item:item[0])
    
    for k, v in dict:
        print(k, "{:.4f}".format(v/cnt*100))
        
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()