import sys 

def mysolution():
    input = sys.stdin.readline
    
def solution():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n = int(input())
        p = [1, 1, 1]
        for i in range(3, n):
            p.append(p[i-2]+p[i-3])
        print('p=',p)
        print(p[n-1])

if __name__=='__main__':
    solution()