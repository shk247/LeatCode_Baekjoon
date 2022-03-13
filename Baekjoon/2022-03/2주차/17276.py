from copy import deepcopy
import sys 

def mysolution():
    input = sys.stdin.readline
    test = int(input())
    
    def change(arr, d):
        new_arr = deepcopy(arr)
        # 주 대각선
        # 가운데 열
        # 부 대각선
        # 가운데 행 
        
    for _ in range(test):
        n, d = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(n)]
        change(board, d)
        
    
def solution():
    input = sys.stdin.readline
    input = sys.stdin.readline
    test = int(input())
    
    def plus_rotate(arr, n):
        num = n//2
        for i in range(n):
            arr[i][i], arr[i][num] = arr[i][num], arr[i][i]
            arr[i][i], arr[i][n-1-i] = arr[i][n-1-i], arr[i][i]
            arr[i][i], arr[num][i] = arr[num][i], arr[i][i]
        
        for i in range(num):
            arr[num][i], arr[num][n-1-i] = arr[num][n-1-i], arr[num][i]
            
        return arr
    
    def minus_rotate(arr, n):
        num = n//2
        for i in range(n):
            arr[i][n-1-i], arr[i][num] = arr[i][num], arr[i][n-1-i]
            arr[i][n-1-i], arr[i][i] = arr[i][i], arr[i][n-1-i]
            arr[i][n-1-i], arr[num][i] = arr[num][i], arr[i][n-1-i]
            
        for i in range(num):
            arr[n-1-i][i], arr[i][n-1-i] = arr[i][n-1-i], arr[n-1-i][i]
        
        return arr
            
    for _ in range(test):
        n, d = map(int, input().split())
        arr = [list(map(int, input().split())) for _ in range(n)]
        r = abs(d)//45
        for _ in range(r):
            if d<0:
                arr = minus_rotate(arr, n)
            else:
                arr = plus_rotate(arr, n)
                
        for i in range(n):
            for j in range(n):
                print(arr[i][j], end=' ')
            print()
        

if __name__=='__main__':
    mysolution()