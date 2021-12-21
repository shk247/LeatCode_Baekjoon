import sys 

def lcm(a, b):
    return a*b//gcd(a,b)

def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a
    
def mysolution():
    input = sys.stdin.readline
    a, b = map(int, input().split())
    print(gcd(a, b))
    print(lcm(a, b))
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()