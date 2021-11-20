from itertools import combinations
 
def mysolution():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        res = 1 
        if a == b:
            print(1)
            continue
        
        while a!=0:
            print("##### a = ",a)
            res *= (a*b)
            a-=1
            b-=1
        
        print(res)

def factorial(n):
    f = 1 
    for i in range(n):
        f * (i+1)
    return f

def solution():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().split())
        print(factorial(b)//factorial(a)*(factorial(a)*factorial(b-a)))

if __name__=='__main__':
    solution()