def gcd(a, b):
    while b>0:
        a, b = b, a%b
    return a

def mysolution():
    n = int(input())
    
    for _ in range(n):
        a, b = map(int, input().split())
        print(a*b // gcd(a,b))

def solution():
    return

if __name__=='__main__':
    mysolution()