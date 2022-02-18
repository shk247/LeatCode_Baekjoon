import sys 
from itertools import combinations

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    total = [i for i in range(n)]
    answer = 1e9
    
    size = n//2 
    
    for com in combinations(range(n), size):
        start = list(com)
        start_sum = 0 
        
        for i in range(size):
            for j in range(i+1, size):
                start_sum += (board[start[i]][start[j]]+board[start[j]][start[i]])
                
        link = [t for t in total if t not in start]
        link_sum = 0 
        for i in range(size):
            for j in range(i+1, size):
                link_sum += (board[link[i]][link[j]]+board[link[j]][link[i]])
                
        answer = min(answer, abs(start_sum-link_sum))
        
    print(answer)
    
def cal_diff(team1, team2): 
    global arr
    sum_team1, sum_team2 = 0, 0
    
    for i in range(len(team1)):
        for j in range(len(team2)):
            sum_team1 += arr[team1[i]][team1[j]]
            sum_team2 += arr[team2[i]][team2[j]]
    
    return abs(sum_team1-sum_team2)
    
def make_team(team1, count, n, start):
    global answer
    
    if count==n//2:
        team2 = [i for i in range(n) if i not in team1]
        cal = cal_diff(team1, team2)
        answer = min(answer, cal)
        
    for i in range(start, n):
        team1.append(i)
        make_team(team1, count+1, n, i+1)
        team1.remove(i)        

def solution():
    input = sys.stdin.readline
    N = int(input())
    global arr
    arr = [list(map(int, input().split())) for _ in range(N)]

    global answer
    answer = int(1e9)
    make_team([], 0, N, 0)
    
    
if __name__=='__main__':
    mysolution()