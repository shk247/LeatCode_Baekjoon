import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    q = 1
    while q**2<n:
        q+=1
    return q-1

def solution():
    input = sys.stdin.readline
    n = int(input())
    start, end = 0, n
    while start<=end:
        mid = (end+start)//2
        if mid**2 == n:
            return mid
        elif mid**2<n:
            start = mid+1
        elif mid**2>n:
            end = mid-1
    return start

if __name__=='__main__':
    print(mysolution())