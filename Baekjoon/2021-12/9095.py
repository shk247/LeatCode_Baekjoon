import sys 


def fun(num):
    if num==1:
        return 1
    elif num==2:
        return 2
    elif num == 3:
        return 4
    else:
        return fun(num-1) + fun(num-2) + fun(num-3)
    
def mysolution():
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        num = int(input())
        print(fun(num))
        

        
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()