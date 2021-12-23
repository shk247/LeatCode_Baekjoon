import sys 

def mysolution():
    input = sys.stdin.readline
    s = int(input())
    for i in range(1,s):
        if (i*(i+1))/2>s:
            print(i-1)
            return
    
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()