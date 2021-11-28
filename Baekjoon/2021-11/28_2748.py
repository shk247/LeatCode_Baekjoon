import sys 

def mysolution():
    input = sys.stdin.readline
    fibo = [0, 1]
    n = int(input())
    for i in range(2,n+1):
        fibo.append(fibo[-1]+fibo[-2])
    print(fibo[-1])
    
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()