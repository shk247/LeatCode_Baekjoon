import sys 
from collections import defaultdict, deque

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    times = [0]*(n+1)
    dict = defaultdict(list)
    
    for i in range(1, n+1):
        l = list(map(int, input().split()))
        times[i] = l[0]
        for num in l[1:]:
            if num!=-1:
                dict[i].append(num)
    
    for i in range(1, n+1):
        if dict[i]:
            visited = [False]*(n+1) 
            tmp = 0    
            for num in dict[i]:
                if not visited[num]:
                    visited[num] = True
                    tmp+=times[num]
            times[i]=tmp
                    
    print(times)
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    times = [0]*(n+1)
    indegree = [0]*(n+1)
    board = [[0]*(n+1) for _ in range(n+1)]
    
    for i in range(1, n+1):
        line = list(map(int, input().split()))
        times[i]=line[0]
        for l in line[1:]:
            if l!=-1:
                indegree[i]+=1
                board[i][l]=1
                
    q = deque()
    
    for i in range(1, n+1):
        if indegree[i]==0:
            q.append(i)
            
    while q:
        num = q.popleft()
        time = 0 
        for i in range(1, n+1):
            if board[i][num]==1:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
            if board[num][i]:
                time = max(time, times[i])
        times[num]+=time
        
    for time in times[1:]:
        print(time)
                
    
if __name__=='__main__':
    solution()