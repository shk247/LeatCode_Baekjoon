import sys 

def mysolution():
    input = sys.stdin.readline
    bingo = [list(map(int, input().split())) for _ in range(5)]
    nums = [list(map(int, input().split())) for _ in range(5)]
    
    def check(arr, num):
        for i in range(5):
            for j in range(5):
                if arr[i][j] == num:
                    arr[i][j] = 0 
                    return
                
    def find(arr):
        for i in range(5):
            for j in range(5):
                print()
                
    cnt = 0
    for i in range(5):
        for j in range(5):
            check(bingo, nums[i][j])
            if cnt>=15:
                find(bingo)
            cnt+=1 
    
def solution():
    input = sys.stdin.readline
    board = dict()
    
    for i in range(5):
        l = list(map(int, input().split()))
        for j in range(5):
            board[l[j]] = [i,j]
    
    nums = [list(map(int, input().split())) for _ in range(5)]
    bingo = [[0]*5 for _ in range(5)]
    cnt = 0 
    
    for i in range(5):
        for j in range(5):
            x, y = board[nums[i][j]]
            bingo[x][y] = 1
            cnt += 1
            bingo_cnt = 0
            for k in range(5):
                if sum(bingo[k])==5:
                    bingo_cnt+=1
                if sum([bingo[l][k] for l in range(5)])==5:
                    bingo_cnt+=1
            if (bingo[0][0]+bingo[1][1]+bingo[2][2]+bingo[3][3]+bingo[4][4]) == 5:
                bingo_cnt+=1
            if (bingo[4][0]+bingo[3][1]+bingo[2][2]+bingo[1][3]+bingo[0][4]) == 5:
                bingo_cnt+=1 
                
            if bingo_cnt>=3:
                print(cnt)
                return
                        
if __name__=='__main__':
    solution()