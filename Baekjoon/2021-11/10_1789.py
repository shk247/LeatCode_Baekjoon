def mysolution(n):
    for i in range(1,n+1):
        if (i*(i+1))/2>n:
            return i-1
    return n

def solution(s):
    n=1
    while n*(n+1)/2 <= s:
        n+=1
    return
        
 
if __name__ == '__main__':
    n = int(input())
    print(mysolution(n))