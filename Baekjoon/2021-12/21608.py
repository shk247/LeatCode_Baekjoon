import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    ans = 0 
    dict ={}
    for _ in range(n**2):
        student = list(map(int, input().split()))
        dict[student[0]] = student[1:]
    print('dict=',dict)
    arr = [[0]*n for _ in range(n)]
    like = 0 
    empty = 0 
    x = 0 
    y = 0 
    
     
def solution():
    input = sys.stdin.readline
    n = int(input())
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    arr = [[0]*n for _ in range(n)]
    dict ={}
    for _ in range(n**2):
        student = list(map(int, input().split()))
        dict[student[0]] = student[1:]

        maxlike = -1 
        maxempty = -1
        x = 0 
        y = 0
        
        for i in range(n):
            for j in range(n):
                if arr[i][j] == 0:
                    likecnt = 0 
                    emptycnt = 0 
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if 0<=nx<n and 0<=ny<n:
                            if arr[nx][ny] in student:
                                likecnt += 1
                            if arr[nx][ny] == 0:
                                emptycnt += 1
                        if maxlike<likecnt or (maxlike==likecnt and maxempty<emptycnt):
                            x = i 
                            y = j 
                            maxlike = likecnt
                            maxempty = emptycnt
       
        arr[x][y] = student[0]
    
    ans = 0 
    
    print('arr=',arr)
    print('dick=',dict)
    
    for i in range(n):
        for j in range(n):
            cnt = 0 
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                print('i=',i,' j=',j,'nx=',nx,' ny=',ny)
                if 0<=nx<n and 0<=ny<n and arr[nx][ny] in dict[arr[i][j]]:
                    cnt += 1
                    
            if cnt==1:
                ans += 1
            elif cnt == 2:
                ans += 10 
            elif cnt == 3:
                ans += 100 
            elif cnt == 4:
                ans += 1000
    print(ans)    

if __name__=='__main__':
    solution()