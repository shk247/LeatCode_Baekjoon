import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    if n<2:
        print(n)
    else:
        print(int(n**(1/2))+1)
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()