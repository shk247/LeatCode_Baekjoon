import sys 

def mysolution():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a, b = set(), set()
    for _ in range(n):
        a.add(input().strip())
    for _ in range(m):
        b.add(input().strip())

    answer = a&b
    
    print(len(answer))
    
    answer = list(answer)
    
    for i in sorted(answer):
        print(i)
        
    
def solution():
    input = sys.stdin.readline

if __name__=='__main__':
    mysolution()