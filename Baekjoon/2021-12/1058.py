import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    dict = defaultdict(list)
    answer = [0]*(n)
    
    for i in range(n):
        friends = list(input())
        for j in range(len(friends)):
            if friends[j]=='Y':
                dict[i].append(j)
                answer[i] += 1
    
    for i in range(n):
        a = dict[i]
        tmp = []
        for j in a:
            b = dict[j]
            tmp.extend([k for k in b if k not in a and k != i])
        answer[i] += len(set(tmp))
    print(max(answer))
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    friend = [list(input()) for _ in range(n)]
    visit = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if j==k:
                    continue
                if friend[j][k] == 'Y' or (friend[j][i]=='Y' and friend[i][k]=='Y'):
                    visit[j][k] = 1
    
    result = 0 
    for i in visit:
        result = max(result, sum(i))
    print(result)

if __name__=='__main__':
    mysolution()