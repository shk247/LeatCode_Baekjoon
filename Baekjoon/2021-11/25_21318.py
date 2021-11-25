import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    level = list(map(int, input().split()))
    q = int(input())

    for _ in range(q):
        start, end = map(int, input().split())
        check = level[start-1:end]
        cnt = 0
        for i in range(len(check)-1):
            if check[i]>check[i+1]:
                cnt += 1
        print(cnt)

def solution():
    input = sys.stdin.readline
    n = int(input())
    level = list(map(int, input().split()))
    answer = [0]*n
    total = 0 
    for i in range(n-1):
        if level[i]>level[i+1]:
            total += 1
        answer[i+1] = total
        
    q = int(input())
    
    for _ in range(q):
        start, end = list(map(int, input().split()))
        print(answer[end-1] - answer[start-1])
    
if __name__=='__main__':
    solution()