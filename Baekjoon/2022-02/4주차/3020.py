import sys 

def mysolution():
    input = sys.stdin.readline
    n, h = map(int, input().split())
    board = [[0]*(n) for _ in range(h)]
    for i in range(n):
        obstacle = int(input())
        if i%2==0:
            for j in range(obstacle):
                board[h-1-j][i]=1
        else:
            for j in range(obstacle):
                board[j][i]=1
                
    answer = [b.count(1) for b in board]
    min_answer = min(answer)
    
    print(min_answer, answer.count(min_answer))
    
def solution():
    n, h = map(int, input().split())

    down = []
    up = []
    for i in range(n):
        if i % 2 == 0:
            down.append(int(input()))
        else:
            up.append(int(input()))

    down.sort()
    up.sort()

    min_count = n
    range_count = 0


    def binary_search(array, target, start, end):
        while start <= end:
            mid = (start + end) // 2

            if array[mid] < target:
                start = mid + 1
            else:
                end = mid - 1

        return start

    for i in range(1, h + 1):
        down_count = len(down) - binary_search(down, i - 0.5, 0, len(down) - 1)
        top_count = len(up) - binary_search(up, h - i + 0.5, 0, len(up) - 1)

        if min_count == down_count + top_count:
            range_count += 1
        elif min_count > down_count + top_count: # 현재 범위가 새로운 최소 값이면
            range_count = 1
            min_count = down_count + top_count

    print(min_count, range_count)
        
if __name__=='__main__':
    solution()