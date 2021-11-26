import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    l = []
    for _ in range(n):
        l.append(int(input()))
    l.sort()
    answer = []
    for i in range(n):
        answer.append(l[i]*(n-i))
    print(max(answer))

def solution():
    input = sys.stdin.readline
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    arr.sort()
    for i in range(n):
        arr[i] = arr[i] * (n-i)
    print(max(arr))

if __name__=='__main__':
    mysolution()