import sys 
from itertools import permutations, combinations

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    nums = [i for i in range(n)]
    half = n//2
    answer = 1e9
    
    for per in list(permutations(nums, n)):
        start, link = 0, 0
        
        for i in range(0, half):
            for j in range(i+1, half):
                a, b = per[i], per[j]
                start += (board[a][b]+board[b][a])
        
        for i in range(half, n):
            for j in range(i+1, n):
                a, b = per[i], per[j]
                link += (board[a][b]+board[b][a])
        
        answer = min(answer, abs(start-link))
        
    print(answer)
            
def solution():
    input = sys.stdin.readline
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    nums = [i for i in range(n)]
    answer = 1e9

    for r1 in list(combinations(nums, n//2)):
        start, link = 0, 0
        r2 = list(set(nums)-set(r1))
        for r in list(combinations(r1, 2)):
            start += (board[r[0]][r[1]]+board[r[1]][r[0]])
        for r in list(combinations(r2, 2)):
            link += (board[r[0]][r[1]]+board[r[1]][r[0]])
        answer = min(answer, abs(start-link))
        
    print(answer)
    
def solution2():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    nums = [i for i in range(n)]
    answer = 1e9
    
    for startList in list(combinations(nums, n//2)):
        start, link = 0, 0
        for x in startList:
            for y in startList:
                start += arr[x][y]
                
        linkList = [i for i in range(n) if i not in startList]
        for x in linkList:
            for y in linkList:
                link += arr[x][y]
        
        answer = min(answer, abs(start-link))
        
    print(answer)
    
def makeTeam(team1, cnt, n, start):
    global answer
    global arr
    if cnt==n//2:
        team2 = [i for i in range(n) if i not in team1]
        sum_team1, sum_team2 = 0, 0
        for i in range(n//2):
            for j in range(n//2):
                sum_team1 += arr[team1[i]][team1[j]]
                sum_team2 += arr[team2[i]][team2[j]]
        answer = min(answer, abs(sum_team1-sum_team2))
        return
    
    for i in range(start, n):
        if i not in team1:
            team1.append(i)
            makeTeam(team1, cnt+1, n, i+1)
            team1.remove(i)
            
def solution3():
    global arr, answer
    
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = 1e9
    makeTeam([], 0, n, 0)
    print(answer)
                
if  __name__=='__main__':
    solution3()