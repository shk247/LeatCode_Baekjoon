import sys 
from collections import defaultdict, deque

def mysolution():
    input = sys.stdin.readline
    testcase_num = int(input())
    
    for _ in range(testcase_num):
        n = int(input())
        rank = list(map(int, input().split()))
        m = int(input())
        case = [list(map(int, input().split())) for _ in range(m)]
        
        dict = defaultdict(list)
        indegree = [0]*(n+1)
        for i in range(n-1):
            dict[rank[i]] = rank[i+1:]
            indegree[rank[i+1]] = i+1
        
        flag = False
        for a,b in case:
            if indegree[a]>indegree[b]:
                indegree[a]-=1
                indegree[b]+=1
                dict[b].remove(a)
                dict[a].append(b)
            else:
                indegree[b]-=1
                indegree[a]+=1
                dict[a].remove(b)
                dict[b].append(a)
                
        q = deque()
        for i in range(1, n+1):
            if indegree[i]==0:
                q.append(i)
        
        while q:
            if len(q)>1:
                print('?')
                break
            num = q.popleft()
            print(num,end=' ')
            for n in dict[num]:
                indegree[n]-=1
                if indegree[n]==0:
                    q.append(n)
        
def solution():
    input = sys.stdin.readline
    testcase_num = int(input())
    
    for _ in range(testcase_num):
        n = int(input())
        rank = list(map(int, input().split()))
        
        dict = defaultdict(list)
        indegree = [0]*(n+1)
        for i in range(n-1):
            dict[rank[i]] = rank[i+1:]
            indegree[rank[i+1]] = i+1
            
        m = int(input())
        for _ in range(m):
            a, b = map(int, input().split())
            if b in dict[a]:
                dict[a].remove(b)
                dict[b].append(a)
                
                indegree[a]+=1
                indegree[b]-=1
            else:
                dict[b].remove(a)
                dict[a].append(b)
                
                indegree[b]+=1
                indegree[a]-=1
                
        q = deque()
        for i in range(1, n+1):
            if indegree[i]==0:
                q.append(i)
       
        answer = []
        while q:
            num = q.popleft()
            answer.append(num)
            for i in dict[num]:
                indegree[i]-=1
                if indegree[i]==0:
                    q.append(i)
        
        if len(answer)==n:
            print(*answer)
        else:
            print('IMPOSSIBLE')
                
                

if __name__=='__main__':
    mysolution()