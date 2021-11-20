import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    total = [0]
    numsum = 0 
    
    for i in l:
        numsum += i
        total.append(numsum)
    for _ in range(m):
        a, b = map(int, input().split())
        print(total[b]-total[a-1])
        

def solution():
    return

if __name__=='__main__':
    mysolution()