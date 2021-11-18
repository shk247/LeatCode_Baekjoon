def mysolution():
    n, m = list(map(int, input().split()))
    str = [ input() for _ in range(n)]
    cnt = 0 
    for _ in range(m):
        if input() in str:
            cnt += 1
    print(cnt)

def solution():
    return

if __name__=='__main__':
    mysolution()