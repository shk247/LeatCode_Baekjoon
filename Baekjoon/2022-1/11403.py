import sys 
from collections import defaultdict

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    check = [0 for _ in range(n)] * n 
    dict = defaultdict(list)
    for i in range(n):
        arr = list(map(int, input().split()))
        for j in range(len(arr)):
            if arr[j]==1:
                dict[i].append(j)

    for i in range(n):
        stack = dict[i]
        while stack:
            num = stack.pop()
            if check[i*n+num] == 0:
                check[i*n+num] = 1 
                stack.extend(dict.get(num))
            else:
                break
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    graph = []
    for i in range(n):
        graph.append(list(map(int, input().split())))
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = 1
                    
    for i in range(n):
        print(*graph[i])
    
            
if __name__=='__main__':
    mysolution()