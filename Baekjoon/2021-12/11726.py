import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    if n<3:
        print(n)
        return
    l = [0]*(n+1)
    l[1]=1
    l[2]=2
    for i in range(3,n+1):
        l[i] = l[i-1]+l[i-2]
    print(l[n]%10007)
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    if n<=3:
        print(n)
        return
    s = [0, 1, 2]
    for i in range(3, n+1):
        s.append(s[i-1]+s[i-2])
    print(s[i]%10007)

if __name__=='__main__':
    solution()