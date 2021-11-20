def mysolution():
    n, m = input().split()
    answer = []
    for _ in range(2):
        answer.extend(list(map(int,input().split())))
    
    for a in sorted(answer):
        print(a,end=' ')

def solution():
    n, m = input().split()
    nmlist = list(map(int, input().split())) + list(map(int, input().split()))
    print(' '.join(map(str, sorted(nmlist))))

if __name__=='__main__':
    mysolution()