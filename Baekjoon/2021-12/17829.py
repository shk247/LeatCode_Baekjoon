import sys 

def mysolution():
    input = sys.stdin.readline
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    polling = []
    size = len(arr)
    while len(polling) != 1:
        for i in range(0, size, 2):
            for j in range(0, size, 2):
                break
    print(arr[:2][:2])    
    # def polling(arr):
        # if len(arr)==1:
        #     return arr[0]
        # size = len(arr)

def search(arr, n):
        if n==1:
            return arr[0][0]
        new_arr = [[] for _ in range(n//2)]
        
        for i in range(0, n, 2):
            for j in range(0, n, 2):
                new_arr[i//2].append(sorted([arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]])[2])
        print('new_arr=',new_arr)
        return search(new_arr, n//2)
    
def solution():
    input = sys.stdin.readline
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]    
    search(arr, n)

if __name__=='__main__':
    solution()