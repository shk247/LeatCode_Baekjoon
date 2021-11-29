import sys 
import re

def mysolution():
    input = sys.stdin.readline
    s = input().strip()
    word = input().strip()
    
    s = ''.join(re.findall('\D+',s))
    
    if word in s:
        print(1)
    else:
        print(0)
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()