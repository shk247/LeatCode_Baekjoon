import sys 

def mysolution():
    input = sys.stdin.readline
    n, l = map(int, input().split())
    x = list(map(int, input().split()))
    
    
def solution():
    input = sys.stdin.readline
    n, l = map(int, input().split())
    x = list(map(int, input().split()))
    s = 0 
    for i in range(n-1, 0, -1):
        s += x[i]
        if not (x[i-1]-l < s/(n-i) < x[i-1]+l):
            print('unstable')
            break
    else:
        print('stable')

if __name__=='__main__':
    mysolution()