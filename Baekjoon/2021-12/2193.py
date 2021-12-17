import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    pinary = [1, 2, 2]
    d = 1
    for i in range(n):
        pinary.append(pinary[-1]+d)
        d+=1
    print(pinary[n-1])
    
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    pinary = [0, 1, 1, 2, 3]
    for i in range(4, n):
        pinary.append(pinary[i-2]+pinary[i-1])
    print(pinary[n])
    

if __name__=='__main__':
    solution()