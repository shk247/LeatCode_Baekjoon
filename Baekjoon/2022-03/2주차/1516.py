from email.policy import default
import sys 
from collections import defaultdict, deque

def mysolution():
    input = sys.stdin.readline

    n = int(input())
    indegree = [0]*(n+1)
    dict = defaultdict(list)
    
    time = [0]*(n+1)    
    for i in range(1, n+1):
        line = list(map(int, input().split()))
        time[i] = line[0]
        for j in line[1:]:
            if j==-1:
                break
            indegree[i]+=1
            dict[j].append(j)
    
    q = deque()
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
            
    while q:
        num = q.popleft()
        for d in dict[num]:
            indegree[d]-=1
            if indegree[d]==0:
                time[d]+=time[num]
                q.append(d)
    
    for t in time[1:]:
        print(t)
    
def solution():
    input = sys.stdin.readline
    N = int(input())
    indegree = [0]*(N+1)
    arr = [[0]*(N+1) for _ in range(N+1)]
    time = [0]*(N+1)
    
    for i in range(1, N+1):
        _input = list(map(int, input().split()))
        time[i] = _input[0]
        for j in _input[1:-1]:
            indegree[i]+=1
            arr[i][j] = 1 
            
    q = deque()
    for i in range(1, N+1):
        if indegree[i]==0:
            q.append(i)
            
    while q:
        num = q.popleft()
        tmp = 0 
        for i in range(1, N+1):
            if arr[i][num]==1:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
            if arr[num][i]==1:
                tmp = max(tmp, time[i])
        time[num] += tmp 
        
    for t in time[1:]:
        print(t)
    
if __name__=='__main__':
    mysolution()