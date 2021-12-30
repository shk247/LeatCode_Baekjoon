import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        if a==b:
            print(1)
        elif a==1:
            print(b)
        else:
            print(b*(a-1)*(b-1))

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num

def solution():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        answer = factorial(m) // (factorial(n)*factorial*(m-n))
        print(answer)

if __name__=='__main__':
    mysolution()