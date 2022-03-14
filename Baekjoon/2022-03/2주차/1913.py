import sys 

def mysolution():
    input = sys.stdin.readline
    
    n = int(input())
    find_num = int(input())
    
    arr = [[0]*n for _ in range(n)]
    x = y = n//2
    find_x, find_y = x, y
    
    cnt = 1
    arr[x][y] = 1
    num = 2
    
    def make_arr():
        nonlocal arr, num, cnt, find_x, find_y, x, y
        while True:
            if cnt%2==0:
                x_sign, y_sign = 1, -1
            else:
                x_sign, y_sign = -1, 1
                
            for _ in range(cnt):
                x += 1*x_sign
                if 0<=x<n:
                    arr[x][y] = num
                    if num == find_num:
                        find_x, find_y = x+1, y+1 
                    num += 1
                else:
                    return
                    
            for _ in range(cnt):
                y += 1*y_sign
                if 0<=y<n:
                    arr[x][y] = num
                    if num == find_num:
                        find_x, find_y = x+1, y+1 
                    num += 1
                else:
                    return
            
            cnt += 1
            
    make_arr()
    
    for a in arr:
        print(*a)
    
    print(find_x, find_y)
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    arr = [[0]*n for _ in range(n)]
    
    move = [[1,0],[0,1],[-1,0],[0,-1]] 
    d = now_x = now_y = 0 
    now_num = n*n
    
    while now_num>0:
        arr[now_x][now_y] = now_num
        if(now_x + move[d][0] < 0 or now_x + move[d][0] >= n or now_y + move[d][1] < 0 or now_y + move[d][1] >= n or arr[now_x+move[d][0]][now_y+move[d][1]] != 0):
            d = (d+1)%4
        now_y += move[d][1] 
        now_x += move[d][0] 
        now_num -= 1

    find_x, find_y = 0, 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == m:
                find_x = i
                find_y = j 
            print(arr[i][j], end=' ')
        print()
    
    print(find_x+1, find_y+1)


if __name__=='__main__':
    solution()