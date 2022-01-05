import sys 
import math 

def mysolution():
    input = sys.stdin.readline
    s = input().strip()
    t = input().strip()
    _s = s 
    _t = t 
    while len(s)!=len(t):
        if len(s)<len(t):
            s += _s
        else:
            t += _t
    
    if s == t :
        print(1)
    else:
        print(0)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()