import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    check = list('ABCDEF')
    
    for _ in range(n):
        s = list(input().strip())
        if ('A' not in s) or ('F' not in s) or ('C' not in s) or (s.count('B') + s.count('D') +s.count('E')>1) or ([i for i in s if i not in check]):
            print('Good')
        else:
            print('Infected!')
            
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()